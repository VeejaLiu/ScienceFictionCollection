#!/bin/bash

# 遍历当前目录下的所有文件
for file in *; do
    # 检查文件是否是常规文件
    if [[ -f "$file" ]]; then
        # 使用iconv转换编码并保存到临时文件
        iconv -f gbk -t utf-8 "$file" > temp.txt && mv temp.txt "$file"
    fi
done