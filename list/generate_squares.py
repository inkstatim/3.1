# task 2: генерация списка квадратов

def generate_squares(n):
    return [x**2 for x in range(1, n+1)]

print(generate_squares(5))  # [1, 4, 9, 16, 25]
# print(generate_squares(int(input("Enter the number of squares: "))))
