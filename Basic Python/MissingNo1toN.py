def missing_number(numbers, n):
    for i in range(1, n + 1):
        if i not in numbers:
            return i

numbers = [1, 4, 3, 5]

print(missing_number(numbers, 5))
