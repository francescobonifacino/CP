
num = int(input('Num: '))

coord = []
for n in range(num):
    l1 = []
    fileIn = input('Value: ')
    data = fileIn.strip().split()
    for i in data:
        l1.append(int(i))
    
    coord.append(l1)

print(coord)


#---------------------------------------------------------------------------------------------------------------------------
#SOLUTION 1 (do not work - time limit exeded)
    
    
# rects = []


# for rect in coord:
#     parziale = []
    
#     for a in range(rect[0],rect[2]+1):
#         for b in range(rect[1],rect[3]+1):
#             if [a,b] not in parziale:
#                 parziale.append([a,b])
    
    
#     rects.append(parziale)

# print(rects)



# punti_possibili = set()
# for rectangle in rects:
#     for point in rectangle:
#         count = 0 
#         for r in rects:
#             for p in r: 
#                 if point == p:
#                     count += 1
                
#         if count >= (num -1):
#             punti_possibili.add(tuple(point))


# punti = min(list(punti_possibili))

# print(punti[0],punti[1])

#--------------------------------------------------------------------------------------------------
# SOLUTION 2 (do not work - time limit exeded)

# possibili_scelte = []
# max_convalidated = 1

# for j in rects:
#     for k in j: # k single couple 
#         rect_convalidated = 1 
#         coppia_considerata = k
#         for n in rects:
#             if j != n:
#                 for m in n: 
#                     coppia_da_confrontare = m
#                     if (coppia_considerata == coppia_da_confrontare):
#                         rect_convalidated += 1
#                         if rect_convalidated > max_convalidated and rect_convalidated == num - 1:
#                             if coppia_considerata not in possibili_scelte:
#                                 possibili_scelte.append(coppia_considerata)
                

# x_y = min(possibili_scelte)

# print(x_y[0],x_y[1])


     

