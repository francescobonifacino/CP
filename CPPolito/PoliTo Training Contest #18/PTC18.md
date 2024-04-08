Contest link: https://codeforces.com/group/w6aXjpwI9u/contest/515641 

Problem A: 
vaso A = a grammi
vaso B = b grammi 
tazza C = up to c grams of water 
azione -> posso prenfere fino a c grammi da un vaso e versarli nell'altro 
Trovare il numero minimo di mossa per cui a == b 

b - a = |n| 
(n / 2) // c (se in (n/2) % c non c'è resto)
(n / 2) // c + 1 (se (n/2) % c c'è resto)


