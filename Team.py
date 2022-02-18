a = int(input())
count = 0
for i in range(a):
    n, m, a = map(int, input().split())
    if n+m+a >= 2:
        count = count+1
print(count)