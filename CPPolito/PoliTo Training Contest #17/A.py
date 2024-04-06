import sys


numTest = int(input())


testCases= []

for n in range(numTest):
    testCases.append(str(input())) #lista di liste di caratteri che sono ogni test case

for case in testCases:
    a = 0
    b = 0
    for letter in case:
        if letter == "A":
            a +=1
        else:
            b +=1

    if a > b:
        print('A') #output A
    else:
        print('B') #output B 
        


