num = int(input())

for x in range(num):
    testInput = input()
    
    t = testInput.strip().split()
    a = int(t[0])
    b = int(t[1])
    c = int(t[2])

    diff = abs(a - b) / 2

    if diff % c == 0:
        print(int(diff // c))
    else:
        print(int(diff // c + 1))
