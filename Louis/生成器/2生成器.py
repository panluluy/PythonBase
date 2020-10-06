"""
https://www.cnblogs.com/alex3714/articles/5765046.html
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，
创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
"""
# gen = (i+1 for i in range(10))
# 可以通过next(gen)，进行调用
# next(gen)
# print("**********")
# 由于next(gen)已经调用过一次生成器，下次调用紧接着上次调用的结果往下去调用
# for i in gen:
#     print(i)

"""
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
"""

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b,end=',')
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(10)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g = fib(10)
print(next(g))
# for i in fib(10):
#     print(i)