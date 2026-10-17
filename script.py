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

收集科幻小说原文，并集中维护在线阅读所需的作者、作品与版本元信息。

**[在线阅读](https://veejaliu.github.io/ScienceFictionCollection-Web/)** · **[阅读器 Web 仓库](https://github.com/VeejaLiu/ScienceFictionCollection-Web)** · **[元信息维护指南](metadata/README.md)**

## 两个仓库的分工

| 项目 | 负责内容 |
| --- | --- |
| [ScienceFictionCollection](https://github.com/VeejaLiu/ScienceFictionCollection)（本仓库） | 作者与系列目录中的小说原文，以及 `metadata/` 中的姓名、简介、语言版本、头像和封面 |
| [ScienceFictionCollection-Web](https://github.com/VeejaLiu/ScienceFictionCollection-Web) | 书架与列表、在线阅读、语言与版本切换、阅读进度、SEO 和 GitHub Pages 发布 |

当前登记 **12 位作者、210 组作品、211 个作品文件**。正文目录与文件名保留原有结构；网页通过 metadata 中的 `directory`、`path` 绑定文件，内部 ID 保持稳定，对外使用可读的 slug。

## 在线阅读与语言版本

阅读器支持简体中文、繁体中文、英文、法语、德语、俄语、日语和韩语界面。界面翻译不等于正文翻译：当前登记的正文均为简体中文，其他语言版本需要收录真实文件，并通过相同的 `workId` 关联。

每本书优先选择当前界面语言，其次英文，最后选择一个已有语言版本；书架、列表与阅读页均保留版本切换。TXT/Markdown 打开后按需加载正文并保存本机阅读进度，EPUB/PDF 提供原始文件入口。目录及网站构建只读取元信息和图片，不批量读取或打包小说正文。

## 元信息与图片

- `metadata/authors.json`：作者 ID、slug、真实目录、多语言姓名、简介和资料来源。
- `metadata/books/<作者 ID>.json`：文件 ID、作品 `workId`、slug、正文路径、语言、格式、系列和封面。
- `metadata/avatars/`、`metadata/covers/`：WebP 头像和封面；头像最长边 160 像素，封面不超过 600 × 900 像素。
- [封面整理清单](metadata/covers/catalog.json)：全部 211 条记录的检索结果，已为 61 条记录整理封面，其中 6 张来自对应 EPUB；未确认的使用生成式封面。清单保留来源、版本说明及图片摘要。

## 维护与更新

在本仓库根目录执行：

```bash
python3 metadata/sync.py
python3 metadata/sync.py --check
python3 script.py
```

同步脚本只读取文件名、路径和文件大小，保留已有元信息字段；移动文件时先更新 `path`，保留文件 ID、作品 `workId` 和 slug。新增作者或翻译版本的字段说明见 [metadata/README.md](metadata/README.md)。

本 README 的作者和文件目录由 `script.py` 自动生成；修改本页介绍时应同步修改脚本中的 `HEADER`，避免下次生成覆盖。

Web 主分支更新后由 GitHub Actions 自动发布。仅修改本仓库元信息时，在 [Web 的 Pages 发布工作流](https://github.com/VeejaLiu/ScienceFictionCollection-Web/actions/workflows/pages.yml) 选择 **Run workflow** 即可重新构建网站；发布会读取本仓库 `master` 的 metadata，正文则在阅读时从本仓库按需获取。

## 来源与权利记录

小说正文、作者头像、出版社封面与应用代码分别保留各自的权利归属。书目或封面来源链接不代表获得开放许可；封面出处与版本匹配说明见整理清单，阅读器自有代码及第三方素材的授权记录见 [Web 仓库说明](https://github.com/VeejaLiu/ScienceFictionCollection-Web#上游来源与应用授权)。


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
