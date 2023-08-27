import random

def shuffle(list):
    aux = 0
    rand = 0
    for i in range(len(list)):
        rand = random.randint(0,len(list)-1)
        aux = list[rand]
        list[rand] = list[i]
        list[i] = aux

def miracleSort(list):
    while True:
          flag = 0
          for i in range(len(list)-1):
               if(list[i] > list[i+1]):
                    flag=1
                    break
          if flag == 0:
               return True



list = [1,2,3,4,5,6,7,8,9,10]
shuffle(list)
print("Initial list =", list)
miracleSort(list)
print("Final list =",  list)