__author__ = 'Louis-Pan'

import pickle

# 方法一：
fp = open('result.pk','rb')
print(pickle.loads(fp.read()))
fp.close()

# 方法二：
with open('result.pk','rb') as f:
    print(pickle.load(f))