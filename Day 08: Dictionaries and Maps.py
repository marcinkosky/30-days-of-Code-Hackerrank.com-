#!/bin/python3

""""
Task
Given [n] names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of
names to query your phone book for. For each [name] queried, print the associated
entry from your phone book on a new line in the form name=phoneNumber; if an entry 
for [name] is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

    Sample Input
        3
        sam 99912222
        tom 11122222
        harry 12299933
        sam
        edward
        harry

    Sample Output
        sam=99912222
        Not found
        harry=12299933
"""

n = int(input())
# you define how many numbers we will have

name_numbers = [input().split() for _ in range(n)]
# you split every pair 'name number' as 'name' and 'number', space is gone
# you could use .split(" ") there, but space is the only sign that divide those words

phoneBook = {k: v for k,v in name_numbers}
# you determine how dictionary is build, key : value for each element in name_numbers
# key : name, value : number

while True:
    try:
        name = input()                                      # now you check for the name
        if name in phoneBook:                               # if name exists in dictionary
            print('{}={}'.format(name, phoneBook[name]))    # prints name=number
        else:
            print('Not found')                              # what happens if name is not \
    except:                                                 # present
        break                                               # after all is done, break
