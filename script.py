import os
import re
import stat
import tempfile
from pathlib import Path

HEADER = """
<div align="center">
<img src="https://socialify.git.ci/VeejaLiu/ScienceFictionCollection/image?description=1&descriptionEditable=%E7%A7%91%E5%B9%BB%E5%B0%8F%E8%AF%B4%E4%BD%9C%E5%93%81%E9%9B%86&font=Bitter&name=1&owner=1&pattern=Floating%20Cogs&stargazers=1&theme=Dark" alt="ScienceFictionCollection" width="640" height="320" />
</div>

# 科幻小说作品集
> 自己收集的科幻小说作品集。
> 
> 在线阅读：https://kehuan.fun
>
> 本readme文件由仓库内script.py脚本自动生成。


## 贡献者名单 Contributors
[![Contributors](https://contrib.rocks/image?repo=VeejaLiu/ScienceFictionCollection)](https://github.com/VeejaLiu/ScienceFictionCollection/graphs/contributors)

"""

SIZE_UNIT = ["B", "KB", "MB", "GB"]


def get_file_size(file_path):
    unit_level = 0
    file_size = os.path.getsize(file_path)
    for i in range(3):
        if file_size > 1000:
            unit_level += 1
            file_size = file_size / 1000
        else:
            break
    return str(round(file_size, 2)) + SIZE_UNIT[unit_level]


def add_books_from_directory(path, indent_level=0):
    """递归生成目录内容；不跟随符号链接或收录隐藏文件。"""
    markdown = ""
    indent = " " * 2 * indent_level  # 生成缩进

    directories = []
    files = []

    for entry in os.scandir(path):
        if entry.name.startswith('.') or entry.is_symlink():
            continue
        if entry.is_dir():
            directories.append(entry.name)
        elif entry.is_file():
            files.append(entry.name)

    # 先写目录，再写文件
    for directory in sorted(directories):
        markdown += f"{indent}- {directory}\n"
        markdown += add_books_from_directory(os.path.join(path, directory), indent_level + 1)
    for file in sorted(files):
        book_size = get_file_size(os.path.join(path, file))
        markdown += f"{indent}- {file} _[{book_size}]_\n"
    return markdown


def generate_readme(root):
    # 只收录符合仓库命名规则的作者目录，避免将工具目录列为作者。
    authors = sorted(
        path.name for path in root.iterdir()
        if path.is_dir() and not path.is_symlink()
        and re.match(r'^\d{3} - .+', path.name)
    )
    markdown = HEADER + "## 作家\n"
    for author in authors:
        anchor = re.sub(r'[^\w\s-]', '', author.lower()).strip()
        anchor = re.sub(r'\s+', '-', anchor)
        markdown += f"- [{author}](#{anchor})\n"

    markdown += """\n## 作品：
<div style="color:gray">（此顺序只代表本仓库先后的添加顺序）</div>

"""
    for author in authors:
        markdown += f"### {author}\n"
        markdown += add_books_from_directory(root / author)

    return markdown + "\n" + """
## Star History

[![Star History Chart](https://star-history.dera.page/svg?repos=VeejaLiu/ScienceFictionCollection&type=Date)](https://star-history.dera.page/#VeejaLiu/ScienceFictionCollection&Date)
"""

def main():
    # 从任何工作目录启动，都更新脚本所在仓库的 README。
    root = Path(__file__).resolve().parent
    target = root / 'README.md'
    content = generate_readme(root).encode('utf-8')
    if target.exists() and target.read_bytes() == content:
        print('README.md 已是最新。')
        return
    mode = stat.S_IMODE(target.stat().st_mode) if target.exists() else 0o644
    # 完整写入后再替换，防止中途中断导致 README 被截断。
    with tempfile.NamedTemporaryFile(dir=root, prefix='.readme-', delete=False) as file:
        temporary = Path(file.name)
        try:
            file.write(content)
            file.flush()
            os.fsync(file.fileno())
            os.fchmod(file.fileno(), mode)
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)
    print('README.md 已更新。')


if __name__ == '__main__':
    main()
