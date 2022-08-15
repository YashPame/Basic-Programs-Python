def Length():
    string = input("Enter a String: ")
    length = len(string)
    print(f"Length of string is {length}")


def reverseString():
    string = input("Enter a String: ")
    reverseStr = string[::-1]
    print(f"Reversal of given string is {reverseStr}")


def Palindrome():
    string = input("Enter a String: ")
    if string == string[::-1]:
        print("Given String is Palindrome")
    else:
        print("Given String not is Palindrome")


def equalCheck():
    string1 = input("Enter a String: ")
    string2 = input("Enter another String: ")
    if string1 == string2:
        print("Given Strings are Equal")
    else:
        print("Given Strings are not Equal")


def SubStringCheck():
    string = input("Enter a String: ")
    subStr = input("Enter a Sub String: ")

    if subStr in string:
        print("Sub string present")
    else:
        print("Substring Not Present")


while True:
    choice = input("Enter 1 to check length of string \n"
                   "Enter 2 to Reverse string\n"
                   "Enter 3 to check Palindrome\n"
                   "Enter 4 to check 2 strings are equal\n"
                   "Enter 5 to check Sub String Present\n"
                   "Enter 6 to exit\n"
                   "Enter: ")

    if choice == '1':
        Length()
    elif choice == '2':
        reverseString()
    elif choice == '3':
        Palindrome()
    elif choice == '4':
        equalCheck()
    elif choice == '5':
        SubStringCheck()
    elif choice == '6':
        exit()
    else:
        print("Invalid Choice Entered")
