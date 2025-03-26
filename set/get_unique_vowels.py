# task 3: получение уникальных гласных

def get_unique_vowels(s):
    vowels = set("aeiou")
    return {char for char in s.lower() if char in vowels}

print(get_unique_vowels("Hello World"))  # {'e', 'o'}
