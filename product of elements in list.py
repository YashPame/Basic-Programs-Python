from functools import reduce
num=[10,20,30]
product=reduce((lambda x,y: x*y),num)
print("Product of numbers is", product)