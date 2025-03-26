# task 1: анаграмма

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
# print(is_anagram(input("Enter a string: "), input("Enter another string: ")))
