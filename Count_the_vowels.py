# Program to count the vowels in an input
# Jackson Blackman
# 2022-09-08

variables = ['a', 'e', 'i', 'o', 'u']
count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

string = input('Please enter a sentence \n:').lower()
for x in string:
    if x in variables:
        count[x] = count[x] + 1

print(count)
