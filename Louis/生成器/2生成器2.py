import time
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib_gen = fib(10)
print("*****************")
print(fib_gen.__next__())
print("#################")
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())
print(fib_gen.__next__())