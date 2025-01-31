list1 = []
n = int(input("Enter a number of elements in list: "))

for i in range(n):
    a = int(input(f"Enter {i+1}th number: "))
    list1.append(a)

for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i],list1[j] = list1[j],list1[i]
print(list1)
print(f"Second largest number is: {list1[-2]}")
