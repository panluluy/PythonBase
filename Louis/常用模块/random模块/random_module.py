__author__ = 'Louis-Pan'
import random

# 随机生成[0,1]之间的浮点数
print(random.random())

# 随机生成[1,3]之间的整数
print(random.randint(1,3))

# 随机生成[1,3）之间的整数
print(random.randrange(1,3))

# 列表中随机选择一个值
print(random.choice(['orange','pear','banana',]))

# 生成验证码
verify_code = ''

for i in range(4):
    current_num = random.randint(0,3)
    if i == current_num:
        tmp = chr(random.randint(65,90))
        verify_code += tmp
    else:
        tmp = random.randint(0,9)
        verify_code += str(tmp)
print(verify_code)