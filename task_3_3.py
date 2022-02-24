'''3.В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.'''

from random import randint 
a = []         
for i in range (20):    
    a.append (randint (-100, 100)) 
print (a)        
internalsum = 0 
maxim = max(a)
minim = min(a)
 
for i in a:   
    if i<maxim and i>minim:
        internalsum+=i  
    
print ('Summa', internalsum)