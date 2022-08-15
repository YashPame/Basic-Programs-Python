num_list = [45, 55, 60, 37, 100, 105, 220]
number = int(input("Enter a number to divide all: "))
result = list(filter(lambda x: (x % number == 0), num_list))
print(f"Number divisible by {number} are", result)
