#!/bin/bash


# 找到目录的路径

DIR_PATH=$1


# 检查是否提供了目录路径

if [ -z "$DIR_PATH" ]; then

    echo "请提供目录路径。"

    exit 1

fi


# 确保目录存在

if [ ! -d "$DIR_PATH" ]; then

    echo "提供的目录不存在。"

    exit 1

fi


# 找到并更改文件扩展名

find "$DIR_PATH" -type f -name "*.md" -exec bash -c 'mv "$0" "${0%.md}.rst"' {} \;


echo "所有.md文件已更改为.rst文件。"
