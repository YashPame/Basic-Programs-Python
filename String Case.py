'''Write a class that stores a string and all its details such as
upper char
lower char
vowels
spaces'''


class String:
    def __init__(self):
        self.string = input("Enter a String: ")
        self.Uppercase = 0
        self.Lowercase = 0
        self.vowels = 0
        self.spaces = 0

        for i in self.string:
            if i.isupper():
                self.Uppercase += 1
            if i.islower():
                self.Lowercase += 1
            if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                self.vowels += 1
            if i == ' ':
                self.spaces += 1
            else:
                pass

        print("Total Uppercase Characters=", self.Uppercase)
        print("Total Lowercase Characters=", self.Lowercase)
        print("Total Vowel Characters=", self.vowels)
        print("Total space Characters=", self.spaces)

String()