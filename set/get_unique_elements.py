# task 1: уникальные элементы списка

def get_unique_elements(lst):
    return list(set(lst))

print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]
