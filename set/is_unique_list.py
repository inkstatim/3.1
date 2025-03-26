# task 2: проверка списка на уникальность

def is_unique_list(lst):
    return len(lst) == len(set(lst))

print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False
