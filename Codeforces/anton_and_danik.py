# https://codeforces.com/contest/734/problem/A

n = int(input())
s = input()

a = s.count('A')
if a > n - a:
    print('Anton')
elif a < n - a:
    print('Danik')
else:
    print('Friendship')
