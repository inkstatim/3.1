# task 5: удаление дублирующих символов

def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result

print(remove_duplicates("programming"))
# print(remove_duplicates(input("Enter a string: ")))
