#!/bin/python3
def func(num):
    return num[2:]
    # strips aways '0b' from the string, for example ASCII 5 is binary: 0b101 
    
n = int(input().strip())
# we strip away unnecessary white spaces since .strip() doesn't contain any sign.

a = max(func(bin(n)).split('0')).count('1')
# bin(n) converts integer into a binary code with 0b
# func() shortens output by 0b, 0b101 -> 101 (1 line)
# .split('0') splits integer into groups of 111
# .count('1') counts how many 111 are there, for example: 1 111 1 > 1 3 1
# max() prints the highest integer, from example above the answer is 3

print(a)
