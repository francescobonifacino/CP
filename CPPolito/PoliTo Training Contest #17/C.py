
num = int(input())


for n in range(num):
    case = []
    inFile= input()
    data = inFile.strip().split()
    for i in data:
        case.append(int(i))

    value = 0
    a = case[0]
    b = case[1]
    n = case[2]

    while (a <= n) and (b <= n):
        if a+b > n :
            value +=1
            break

        if a > b:
            b = a + b
        else:
            a = a + b
        
        value +=1
    
    print(value)




    








