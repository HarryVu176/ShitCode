# https://codeforces.com/contest/263/problem/A

# get 1 position
for i in range(5):
    a = input().split()
    if '1' in a:
        print(abs(i - 2) + abs(a.index('1') - 2))
