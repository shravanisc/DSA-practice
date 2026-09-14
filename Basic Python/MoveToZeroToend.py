def move_zeros(arr):
    result = []

    for x in arr:
        if x != 0:
            result.append(x)

    for x in arr:
        if x == 0:
            result.append(x)

    return result


arr = [1, 0, 3, 0, 5, 0, 2]
print(move_zeros(arr))
