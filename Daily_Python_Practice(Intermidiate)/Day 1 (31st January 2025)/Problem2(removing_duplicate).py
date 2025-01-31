#Random list
list1 = [1,1,3,4,56,7,1,8,9,10,11]
list2 = []

for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
        
print(list2)
