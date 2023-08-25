import random

def shuffle(list):
    k=0
    aux=0
    for i in range(len(list)):
        k = random.randint(0,len(list)-1)
        aux = list[i]
        list[i] = list[k]
        list[k] = aux

def selectionSort(list):
    aux = 0
    for i in range(len(list)):
        smallestNum = i
        for j in range(i, len(list)):
            if(list[smallestNum] > list[j]):
                smallestNum = j
        aux = list[i]
        list[i] = list[smallestNum]
        list[smallestNum] = aux

print("Selection sort algorithm")
list = [1,2,3,4,5,6,7,8,9,10] 
shuffle(list)
print("Initial list =", list)
selectionSort(list)
print("Final list =", list)
print("Con = 1")



