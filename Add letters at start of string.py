def string(str):
    if str[:2] == 'Is' or str[:2] == 'is':
        return str
    return "Is" + str


print(string("Array"))
print(string("IsBool"))
