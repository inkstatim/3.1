# task 3: объединение двух списков без дубликатов

def merge_lists(list1, list2):
    return list(set(list1 + list2))

print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]
