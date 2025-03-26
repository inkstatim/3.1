# task 4: группировка по первой букве

def group_by_first_letter(strings):
    grouped = {}
    for word in strings:
        key = word[0]
        grouped.setdefault(key, []).append(word)
    return grouped

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
