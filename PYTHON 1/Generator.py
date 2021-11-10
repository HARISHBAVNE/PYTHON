def gen(n):
    for i in range(1,n+1):
        yield (i)

num = gen(10)

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))