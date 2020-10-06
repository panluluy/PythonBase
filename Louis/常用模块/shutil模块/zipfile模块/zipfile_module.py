__author__ = 'Louis-Pan'

import zipfile

# 压缩文件
z = zipfile.ZipFile('test.zip','w')
z.write(r'D:\Louis\常用模块\shutil模块\a')
print("================")
z.write(r'D:\Louis\常用模块\shutil模块\b')
z.close()

# 解压文件
file = zipfile.ZipFile('test.zip','r')
file.extractall(r'D:\Louis\常用模块\shutil模块\zipfile模块\aaa')
file.close()