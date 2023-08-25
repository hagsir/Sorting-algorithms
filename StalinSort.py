import random

def shuffle(list):
    k=0
    aux=0
    for i in range(len(list)):
        k = random.randint(0,len(list)-1)
        aux = list[i]
        list[i] = list[k]
        list[k] = aux

def stalinSort(list):
    newList=[]
    num=list[0]
    for i in range(len(list)):
        if(list[i] < num):
            list[i] = 0
            

list = [1,2,3,4,5,6,7,8,9,10]
shuffle(list)
print("Initial list =", list)
stalinSort(list)
print(list)
