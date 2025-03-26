# task 1: частотный анализ строки

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
