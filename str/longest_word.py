# task 3: самое длинное слово

def longest_word(s):
    words = s.split()
    return max(words, key=len)

print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))  # "extraordinary"
