str = input("Enter String: ")
try:
    i = float(str)
    print("Numeric")
except(ValueError, TypeError):
    print('Not Numeric')
print()
