contest link: https://codeforces.com/contest/1955

## Problema A:

1 piece = a 
2 piece = b (promozione)

Uno deve comprare esattamente n pezzi 
Comprando 2 pezzi si può decidere se pagarli al prezzo normale o col prezzo in promozione 
Quanto è il minimo che può spendere per comprare n pezzi? 

Prima cosa da controllare -> se 2a < b, cioè se due pezzi singoli al prezzo normale costano meno di 2 pezzi in promozione.
Se 2a <= b, allora compra tutti gli n pezzi a prezzo normale
se 2a > b, compra più pezzi possibili con la promozione e il restante a prezzo normale 
