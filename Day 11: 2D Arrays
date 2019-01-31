#!/bin/python3
arr = [list(map(int, input().rstrip().split())) for _ in range(6)]

print(max(sum(arr[i][j:j+3] + [arr[i+1][j+1]] + arr[i+2][j:j+3]) for j in range(len(arr)-2) for i in range(len(arr)-2)))
