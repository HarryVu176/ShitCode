# https://codeforces.com/contest/231/problem/A

n = int(input())
o = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        o += 1
print(o)
