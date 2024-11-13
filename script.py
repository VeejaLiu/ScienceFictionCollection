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
        dirName = f.name
        author_path_name_list.append(dirName)

author_path_name_list.sort()

markdown += f"""## 目前作家\n"""
for author_path_name in author_path_name_list:
    markdown += f"""- {author_path_name}\n"""

markdown += f"""\n"""
markdown += f"""
## 目前作品：
<div style="color:gray">
（此顺序只代表本仓库先后的添加顺序）
</div>

"""

SIZE_UNIT = [
    "B",
    "KB",
    "MB",
    "GB"
]


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


# 遍历所有的作者目录
for author_path_name in author_path_name_list:
    markdown += f"""### {author_path_name}\n"""
    author_path = "./" + author_path_name
    author_series_list = []
    author_book_info_list = []
    # 遍历一个作者下面的所有文件
    for file in os.scandir(author_path):
        file_name = file.name
        file_path = author_path + '/' + file_name
        # 如果是个目录，存入系列目录列表
        if file.is_dir():
            author_series_list.append({'file_path': file_path, 'file_name': file_name})
        # 如果是个文件，存入书籍列表
        else:
            book_size = get_file_size(file_path)
            author_book_info_list.append(file.name + f'     _[{book_size}]_')

    # 如果该作者目录下面有系列目录
    if len(author_series_list) > 0:
        # TODO 排序没有做好
        # author_series_list.sort()
        # 遍历作者的每一个系列目录
        for author_series in author_series_list:
            series_name = author_series['file_name']
            series_path = author_series['file_path']
            markdown += f"""- {series_name}\n"""
            book_info_list = []
            for file in os.scandir(series_path):
                book_name = file.name
                book_path = series_path + '/' + book_name
                book_size = get_file_size(book_path)
                book_info_list.append(book_name + f'     _[{book_size}]_')
            book_info_list.sort()
            for book_info in book_info_list:
                markdown += f"""  - {book_info}\n"""

    # 遍历作者的每一本书
    author_book_info_list.sort()
    for file_name in author_book_info_list:
        markdown += f"""- {file_name}\n"""
    markdown += f"""\n"""

print(markdown)

with open("README.md", "w") as file:
    file.write(markdown)
