import os

markdown = """# 科幻小说作品集
自己收集的科幻小说作品集。

# 目前作品：
（此顺序只代表本仓库先后的添加顺序）
"""

excludePath = ['venv', '.git', '.idea']

child_path_name_list = []

for f in os.scandir():
    filename = f.name
    if f.is_dir() and filename not in excludePath:
        dirName = f.name
        child_path_name_list.append(dirName)

child_path_name_list.sort()

for child_path_name in child_path_name_list:
    markdown += f"""## {child_path_name}\n"""
    child_path = "./" + child_path_name
    for file in os.scandir('./' + child_path_name):
        markdown += f"""- {file.name}\n"""
    markdown += f"""\n"""

print(markdown)

with open("README.md", "w") as file:
    file.write(markdown)
