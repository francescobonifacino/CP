
num = int(input())
VALORI_MATRICE = ['A','B','C']
testCases = []

for n in range(num):
    test = []
    for i in range(3):
        line = str(input())
        test.append(line)

    testCases.append(test)

for case in testCases:
    qm_line = 0
    qm_column = 0
    for j in range(3):
        if '?' in case[j]:
            qm_line = j
    
    for k in range(3):
        if case[qm_line][k] == '?':
            qm_column = k 
    
    #ho trovato la posizione precisa nella matrice del ?
    #il ? è all'incrocio di una riga e di una colonna, in quella riga e colonna il valore corrispondente a ? è lo stesso
    insieme = set()
    for letter in case[qm_line]:
        if letter != '?':
            insieme.add(letter)
    
    for linea in case:
        if linea[qm_column] != '?':
            insieme.add(linea[qm_column])
    
    for char in VALORI_MATRICE:
        if char not in insieme:
            print(char)


    
    

