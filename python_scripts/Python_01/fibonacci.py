import sys

a, b = 0, 1
limit = int(sys.argv[1])
while b < limit:
    print(b)
    a, b = b, a+b


def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
        return result
