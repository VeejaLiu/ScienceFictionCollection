#!/bin/bash

# 打印函数, 绿色
function print() {
    echo -e "\033[32m[Info] $1\033[0m"
}

# 打印函数, 红色
function print_error() {
    echo -e "\033[31m[Error] $1\033[0m"
}

# 打印函数, 黄色
function print_warn() {
    echo -e "\033[33m[Warn] $1\033[0m"
}


# 遍历当前目录下的所有文件
for file in *; do
    # 输出文件名
    print "File: $file"

    # 文件名不是txt结尾的文件跳过
    if [[ "${file##*.}" != "txt" ]]; then
        print_warn "Not a txt file, skip."
        continue
    fi

    # 检查文件是否是常规文件
    if [[ -f "$file" ]]; then
        # 使用iconv转换编码并保存到临时文件
        iconv -f gbk -t utf-8 "$file" > temp.txt
        # 替换原文件
        mv temp.txt "$file"
    fi
done