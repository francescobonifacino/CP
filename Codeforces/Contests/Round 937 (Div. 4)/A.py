

num = int(input('Num: '))

for i in range(num):
    testCase = input('Input: ')

    x = testCase.strip().split()
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])

    if a < b and b < c:
        print('STAIR')
    elif a < b and c < b:
        print('PEAK')
    else:
        print('NONE')



