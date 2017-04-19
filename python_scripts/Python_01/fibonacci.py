import sys

a, b = 0, 1
limit = int(sys.argv[1])
while b < limit:
    print(b)
    a, b = b, a+b
