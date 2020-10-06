__author__ = 'Louis-Pan'

import json

data = {
    "name":"pll",
    "age":18,
    'tel':123456
}

# 方法一
with open('result.json','w+') as fp:
    json.dump(data,fp)


# 方法二：
f = open('result.json','w')
f.write(json.dumps(data))
f.close()


