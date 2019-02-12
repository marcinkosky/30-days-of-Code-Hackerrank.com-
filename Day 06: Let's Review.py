#!/bin/python3

"""
    HackerRank, Day 6: Let's Review

    *Objective*
    Today we're expanding our knowledge of Strings and combining it with what
    we've already learned about loops. 

    *Task*
    Given a S string, N, of length that is indexed from 0 to N-1, print its 
    even-indexed and odd-indexed characters as space-separated strings on a
    single line (see the sample below for more detail).

    Note:
    0 is considered to be an even index.

    *Input Format*
    The first line contains an integer, (the number of test cases).
    Each line i of the T subsequent lines contain a String, S.

    *Sample Input*
        2
        Hacker
        Rank

    *Sample Output*
        
        Hce akr
        Rn ak
    
    Used pages:
    https://www.pythoncentral.io/pythons-range-function-explained/

"""

for N in range(int(input())):
    # you define an integer N
    # i.e. range(3) == [0, 1, 2]
    # N means how many words per iteration you will separate

    S = input()
    # you define a string

    print(S[::2], S[1::2])
    # this command prints two variables, separated by coma 'x, y'
    
    # (string[::2]) prints your string, by every two characters from 1st character
    # (string[1::2]) prints your string, by every two characters from 2nd character
