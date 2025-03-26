# task 2: палиндром

def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("racecar"))                         # True
print(is_palindrome("hello"))                           # False
# print(is_palindrome(input("Enter a string: ")))