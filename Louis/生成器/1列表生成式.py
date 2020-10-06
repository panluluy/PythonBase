# 方法一：
a = [0,1,2,3,4,5,6,7,8,9]
b = []
for i in a:
    b.append(i+1)
print(b)

# 方法二
m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index,i in enumerate(m):
    m[index] = i+1
print(m)

# 方法三
print([i+1 for i in range(10)])