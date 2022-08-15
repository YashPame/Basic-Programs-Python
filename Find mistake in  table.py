# Mistake find in Table

import random


def wrongMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(1, 3)
    return table

def correctMultiplication(table, number):
    for i in range(1,11):
        if table[i-1]!=i*number:
            return i-1
    return None
if __name__ == "__main__":
    number = int(input(" Enter number: "))
    wrongTable = wrongMultiplication(number)
    print(wrongTable)
    wrongIndex= correctMultiplication(wrongTable, number)
    print(f"Table is wrong as index {wrongIndex}")
