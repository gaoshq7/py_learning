#### 基本规范 ####

# 1. 脚本开头标明编码集：‘# -*- coding: utf-8 -*-’。
# 2. 脚本说明文档按照所示格式使用“三引号”进行编写。

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""示例文档字符串。

该模块演示由'谷歌Python指定的文档风格指南_。文档字符串可以扩展到多行。节被创建带有部分标题和冒号，后面跟着一段缩进文本。

例子:
    可以用“Example”或“Examples”来给出例子。
    节支持任何reStructuredText格式，包括
    文字块::

        $ python example_google.py

分节符是通过恢复未缩进的文本创建的。分节符也是在新部分开始时隐式创建的。
"""
import os


def list_files(directory: str):
    """列出指定目录下的所有文件路径"""
    if not os.path.exists(directory):
        print(f"❌ 目录不存在: {directory}")
        return

    for root, dirs, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            print(filepath)


# 示例：列出当前目录下的所有文件
if __name__ == "__main__":
    list_files(".")