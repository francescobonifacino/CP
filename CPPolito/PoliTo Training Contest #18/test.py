

def main():
    print(is_strongly_composed(4))

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