# Basic Questions
# Q. Write a Python program to check number is prime or not.

num = int(input("Enter a number to check Prime: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is Not Prime")
            break
    else:
        print(num, "is Prime")
else:
    print(num, "is Not prime")
