def missing_number(numbers):
    for i in range(1, 6):
        if i not in numbers:
            return i


numbers = [1, 4, 3, 5]

print(missing_number(numbers))
