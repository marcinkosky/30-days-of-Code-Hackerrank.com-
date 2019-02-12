#!/bin/python3
numSwaps = 0
n = int(input())
a = list(map(int, input().strip().split(' ')))

for i in range(n):
    for x in range(len(a)-1):
        if a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]
            numSwaps += 1

print(f'Array is sorted in {numSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[-1]}')
