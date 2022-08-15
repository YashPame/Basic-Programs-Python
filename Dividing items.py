# Dividing The Apples

apples= int(input("Enter the number of apples: "))
mn= int(input("Enter minimum number to check: "))
mx= int(input("Enter maximum number to check: "))


for i in range(mn, mx+1):
    if apples%i==0:
        print(f"{i} is divisor of {apples}")
    else:
        print(f"{i} is not divisor of {apples}")




