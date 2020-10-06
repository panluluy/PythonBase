__author__ = 'Louis-Pan'
import pickle

info = {
    "name":"pll",
    "age":18,
    'tel':123456
}

# 方法一：
# pickle.dumps(info)返回的是字节形式所以需要使用wb模式打开文件
fp = open('result.pk','wb')
fp.write(pickle.dumps(info))
fp.close()

# 方法二：
with open('result.pk','wb') as f:
    pickle.dump(info,f)
