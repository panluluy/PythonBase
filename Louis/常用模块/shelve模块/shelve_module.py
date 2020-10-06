__author__ = 'Louis-Pan'

import shelve

# 打开shelve模块的句柄
f = shelve.open('shelve.txt')

info = {'name':'pll','age':'123'}
list = ['a','b','c','d']

# 将字典和列表存储到文件中
f['info'] = info
f['list'] = list
f.close()

# 打开文件的句柄
fp = shelve.open('shelve.txt')
# 获取键对应的值
print(fp.get('info'))
print(fp.get('list'))
fp.close()