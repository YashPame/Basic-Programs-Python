# Result calculation of 5 subjects

# Taking Marks in 5 subjects as input
s1 = int(input("Enter marks in subject 1: "))
s2 = int(input("Enter marks in subject 2: "))
s3 = int(input("Enter marks in subject 3: "))
s4 = int(input("Enter marks in subject 4: "))
s5 = int(input("Enter marks in subject 5: "))

# Calculating total marks and Percentage and displaying them
total = s1 + s2 + s3 + s4 + s5
percentage = (total / 500) * 100

print("Total marks obtained: ", total)
print("Total Percentage: ", percentage, "%")

# Checking passing Class and individual subject aggregate
if s1 >= 40 and s2 >= 40 and s3 >= 40 and s4 >= 40 and s5 >= 40:
    if percentage >= 75:
        print('You Passed with Distinction')
    elif 75 > percentage >= 60:
        print('You Passed with First Class')
    elif 60 > percentage >= 50:
        print('You Passed with Second Class')
    else:
        print('You Passed with Third Class')

else:
    print("Failed!")

