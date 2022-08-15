# Reverse the list
# 3 methods
print("Enter the number of list one by one: ")
size = int(input("Enter size of list: "))
list = []
for i in range (size):
    list.append(int(input("Enter list element: ")))

print(f"Your list is {list}")

#Reversing
reverse1=list[:]
reverse1.reverse()
print(reverse1)
print(list[::-1])

reverse3=list[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3)-i-1]= reverse3[len(reverse3)-i-1], reverse3[i]

print(reverse3)

