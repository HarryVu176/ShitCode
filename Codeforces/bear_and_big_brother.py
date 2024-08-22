# https://codeforces.com/contest/791/problem/A
import math

a, b = map(float, input().split())
c = 0
if a == b:
    print(1)
else:
    c = math.ceil(math.log(b / a, 3 / 2))
    if a * (3 ** c) <= b * (2 ** c):
        c += 1
    print(c)
