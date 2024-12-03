import os

markdown = """
<div align="center">
<img src="https://socialify.git.ci/VeejaLiu/ScienceFictionCollection/image?description=1&descriptionEditable=%E7%A7%91%E5%B9%BB%E5%B0%8F%E8%AF%B4%E4%BD%9C%E5%93%81%E9%9B%86&font=Bitter&name=1&owner=1&pattern=Floating%20Cogs&stargazers=1&theme=Dark" alt="ScienceFictionCollection" width="640" height="320" />
</div>

# 科幻小说作品集
> 自己收集的科幻小说作品集。
>
> 本readme文件由仓库内script.py脚本自动生成。
"""

excludePath = ['venv', '.git', '.idea']

author_path_name_list = []

# 获取所有的作者目录
for f in os.scandir():
    filename = f.name
    if f.is_dir() and filename not in excludePath:
        author_path_name_list.append(f.name)

author_path_name_list.sort()

markdown += f"""## 目前作家\n"""
for author in author_path_name_list:
    markdown += f"""- {author}\n"""

markdown += f"""\n## 目前作品：
<div style="color:gray">（此顺序只代表本仓库先后的添加顺序）</div>

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
    """递归遍历目录，添加书籍和系列信息到 markdown。"""
    global markdown
    indent = " " * 2 * indent_level  # 生成缩进

    directories = []
    files = []

    for entry in os.scandir(path):
        if entry.is_dir():
            directories.append(entry.name)
        else:
            files.append(entry.name)

    # 先写目录，再写文件
    for directory in sorted(directories):
        markdown += f"{indent}- {directory}\n"
        add_books_from_directory(os.path.join(path, directory), indent_level + 1)
    for file in sorted(files):
        book_size = get_file_size(os.path.join(path, file))
        markdown += f"{indent}- {file} _[{book_size}]_\n"


# 遍历所有作者的目录
for author in author_path_name_list:
    markdown += f"""### {author}\n"""
    author_path = os.path.join(".", author)
    add_books_from_directory(author_path)

markdown += f"""\n"""

markdown += f"""
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=VeejaLiu/ScienceFictionCollection&type=Date)](https://star-history.com/#VeejaLiu/ScienceFictionCollection&Date)
"""

print(markdown)

with open("README.md", "w") as file:
    file.write(markdown)
