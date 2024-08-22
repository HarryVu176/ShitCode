# https://codeforces.com/contest/677/problem/A

a, b = map(int, input().split())
c = list(map(int, input().split()))

for h in c:
    if h > b:
        a += 1

print(a)
