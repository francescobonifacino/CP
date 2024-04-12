

def main():
    num = int(input('num: '))

    for i in range(num):
        n = int(input('n: '))
        x = input('valori: ')
        x1 = x.strip().split()
        a = []
        for z in x1:
            a.append(int(z))

        prodotto = 1
        for w in range(n):
            prodotto = prodotto *a[w]
        
                            
        
        print(b)
                    




    

def is_strongly_composed(numero):
    divisori = []
    primi= 0 
    compositi = 0 
    for x in range(2,numero +1):
        if numero % x == 0:
            divisori.append(x)

            div = 0
            for y in range(1,x+1):
                if x % y == 0:
                    div += 1
            
            if div == 2:
                primi +=1
            else:
                compositi += 1
    
    if primi <= compositi:
        return 0
    else:
        return 1

    
    
        
    
main()