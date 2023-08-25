import random

def shuffle(list):
    k=0
    aux=0
    for i in range(len(list)):
        k = random.randint(0,len(list)-1)
        aux = list[i]
        list[i] = list[k]
        list[k] = aux

def bubbleSort(list):
    aux=0
    for i in range(len(list)-1):
        if(list[i]>list[i+1]):
            aux = list[i]
            list[i] = list[i+1]
            list[i+1] = aux

def isSorted(list):
    for i in range(len(list)-1):
        if(list[i] > list[i+1]):
            return False
    return True


con = 0
list = [1,2,3,4,5,6,7,8,9,10] 
shuffle(list)

while True:
    bubbleSort(list)
    con+=1
    if(isSorted(list)):
        break

print(con)