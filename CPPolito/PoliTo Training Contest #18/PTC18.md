Contest link: https://codeforces.com/group/w6aXjpwI9u/contest/515641 

## Problema A: 
vaso A = a grammi
vaso B = b grammi 
tazza C = up to c grams of water 
azione -> posso prenfere fino a c grammi da un vaso e versarli nell'altro 
Trovare il numero minimo di mossa per cui a == b 

b - a = |n| 
(n / 2) // c (se in (n/2) % c non c'è resto)
(n / 2) // c + 1 (se (n/2) % c c'è resto)


## Problema B: 
ho una stringa binaria s (0101011010)

2 operazioni:
- cancellare 1 carattere dalla stringa (1 coin cost)
- scambiare qualunque paio di caratteri (0 coin cost)
Sia t una stringa ottenuta da operazioni su s tale che ogni t(i) = s(i) (cioè ogni carattere sia diverso dala stringa origianria)
Calcolare il costo totale per ottenere t

Prima trovo quanti 0 e quanti 1 ci sono nella stringa (se num di 0 == num di 1 allora sono solo operazioni di swap (costo zero))

per ogni carattere (posso fare uno swap? si -> num di 0 o num di 1 -1, non posso farlo? coin + 1)