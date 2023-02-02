import os

markdown = """
<div align="center">
<img src="https://socialify.git.ci/VeejaLiu/ScienceFictionCollection/image?description=1&descriptionEditable=%E7%A7%91%E5%B9%BB%E5%B0%8F%E8%AF%B4%E4%BD%9C%E5%93%81%E9%9B%86&font=Bitter&name=1&owner=1&pattern=Floating%20Cogs&stargazers=1&theme=Dark" alt="ScienceFictionCollection" width="640" height="320" />
</div>

# 科幻小说作品集
> 自己收集的科幻小说作品集。
"""

excludePath = ['venv', '.git', '.idea']

child_path_name_list = []

for f in os.scandir():
    filename = f.name
    if f.is_dir() and filename not in excludePath:
        dirName = f.name
        child_path_name_list.append(dirName)

child_path_name_list.sort()

markdown += f"""## 目前作家\n"""
for child_path_name in child_path_name_list:
    markdown += f"""- {child_path_name}\n"""

markdown += f"""\n"""
markdown += f"""
## 目前作品：
<div style="color:gray">
（此顺序只代表本仓库先后的添加顺序）
</div>

"""

for child_path_name in child_path_name_list:
    markdown += f"""### {child_path_name}\n"""
    child_path = "./" + child_path_name
    for file in os.scandir('./' + child_path_name):
        markdown += f"""- {file.name}\n"""
    markdown += f"""\n"""

print(markdown)

with open("README.md", "w") as file:
    file.write(markdown)
