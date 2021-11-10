import m 

print(m.A)
print(m.B)
print(m.C)

def add(*args):
    add1 = 0
    for i in (args):
        add1 += i
    print(add1)
add(m.A,m.B,m.C)
