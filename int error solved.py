while True:
    try:
        a=int(input("Enter a number: "))
        break
    except ValueError:
        print("This is not a integer, Try again....")