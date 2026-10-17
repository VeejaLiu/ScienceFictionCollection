#!/bin/bash

# 用法：bash convert.sh [文件或目录 ...]
# 默认递归处理当前目录的 *.txt；仅将严格可逆的 GBK 转为 UTF-8。
# 已是 UTF-8 的文件保持原样；无法解码的文件报错且不覆盖。
set -euo pipefail

exec python3 - "$@" <<'PY'
import os
import stat
import sys
import tempfile
from pathlib import Path


def find_text_files(path):
    if path.is_symlink():
        return
    if path.is_dir():
        for child in sorted(path.iterdir()):
            if not child.name.startswith('.'):
                yield from find_text_files(child)
    elif path.is_file():
        if path.suffix.lower() == '.txt':
            yield path
    else:
        raise ValueError(f'路径不存在或不是普通文件：{path}')


def convert(path):
    original = path.read_bytes()
    try:
        original.decode('utf-8')
        return False
    except UnicodeDecodeError:
        pass

    # 严格解码，不忽略错误、不替换字符、不规范化换行。
    text = original.decode('gbk')
    if text.encode('gbk') != original:
        raise ValueError('GBK 编码无法逐字节还原，已跳过')
    converted = text.encode('utf-8')
    if converted.decode('utf-8').encode('gbk') != original:
        raise ValueError('转换校验失败，已跳过')

    mode = stat.S_IMODE(path.stat().st_mode)
    # 每个文件使用独立的临时文件；只有写入和校验成功才原子替换。
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix='.convert-', delete=False) as file:
        temporary = Path(file.name)
        try:
            file.write(converted)
            file.flush()
            os.fsync(file.fileno())
            os.fchmod(file.fileno(), mode)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        if temporary.read_bytes() != converted:
            raise ValueError('临时文件校验失败，原文件保持不变')
        if path.read_bytes() != original:
            raise ValueError('处理期间原文件发生变化，已取消替换')
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'[已转换] {path}')
    return True


converted_count = 0
skipped_count = 0
errors = 0
seen = set()
for argument in sys.argv[1:] or ['.']:
    try:
        for path in find_text_files(Path(argument)):
            key = path.resolve()
            if key in seen:
                continue
            seen.add(key)
            try:
                if convert(path):
                    converted_count += 1
                else:
                    skipped_count += 1
            except (OSError, UnicodeError, ValueError) as error:
                errors += 1
                print(f'[失败，保留原文件] {path}: {error}', file=sys.stderr)
    except (OSError, ValueError) as error:
        errors += 1
        print(f'[失败] {argument}: {error}', file=sys.stderr)

print(f'完成：转换 {converted_count}，跳过 UTF-8 文件 {skipped_count}，失败 {errors}。')
sys.exit(1 if errors else 0)
PY
