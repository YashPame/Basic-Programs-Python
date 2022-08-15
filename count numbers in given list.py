def counting(nums):
    count = 0
    a = int(input("Enter number to count: "))
    for num in nums:
        if num == a:
            count = count + 1
    return count


print(counting([1, 4, 4, 5, 6, 9, 4, 5]))
print(counting([1, 7, 9, 5, 6, 3, 2]))
