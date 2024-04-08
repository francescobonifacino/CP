num = int(input())

for x in range(num):
    testInput = input()
    t = testInput.strip().split()
    n = int(t[0])
    a = int(t[1])
    b = int(t[2])

    if 2*a <= b:
        print(n*a)
    else:
        n_prom = n // 2
        if n % 2 == 0:
            print(n_prom * b)
        else:
            print(n_prom * b + a) 