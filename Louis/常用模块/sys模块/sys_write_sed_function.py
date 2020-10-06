__author__="Louis-Pan"
"""
在命令行中输入python sys_write_sed_function.py Jmeter Loadrunner
"""

import sys

f = open('abc.txt','r',encoding='utf-8')
f_new = open('abc_bak.txt','w',encoding='utf-8')

find_str = sys.argv[1]
new_str = sys.argv[2]
for line in f:
    if find_str in line:
        line = line.replace(find_str,new_str)
    f_new.write(line)
f.close()
f_new.close()