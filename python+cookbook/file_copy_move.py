#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题
你想要复制或移动文件和目录，但是又不想调用 shell 命令。
解决方案
shutil 模块有很多便捷的函数可以复制文件和目录。使用起来非常简单，比如：
"""
import shutil
src=r'C:\Users\liming\Desktop\新建文本文档.txt'
dst=r'C:\Users\liming\Desktop\workspace'
# Copy src to dst .(cp src dst)
shutil.copy(src,dst)

# Copy files ,but preserue metadata (cp -p sec dst)
shutil.copy2(src,dst)

# Copy directory tree (cp -R src dst)
shutil.copytree(src,dst)

# Move src to dst (mv src dst)
shutil.move(src,dst)

