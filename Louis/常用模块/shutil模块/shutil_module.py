__author__ = 'Louis-Pan'

import shutil

f1 = open('a','r+',encoding='utf-8')
f2 = open('b','w+',encoding='utf-8')

# 复制a文件中的内容至b文件中
shutil.copyfileobj(f1,f2)

# 复制a文件中的内容至c文件中，c文件不存在直接创建，存在直接覆盖
shutil.copyfile('a','c')

# 复制目录及文件
shutil.copytree('广东','广东_copy')

# 删除目录
shutil.rmtree('广东_copy')

# 压缩目录
shutil.make_archive('shutil','zip',r'D:\Louis\常用模块\random模块')