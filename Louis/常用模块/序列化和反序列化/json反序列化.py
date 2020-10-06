__author__ = 'Louis-Pan'

import json

# 方法一：
with open('result.json','r+') as fp:
    result = json.load(fp)
    print(type(result))

# 方法二：
fp = open('result.json','r')
print(json.loads(fp.read()))
fp.close()