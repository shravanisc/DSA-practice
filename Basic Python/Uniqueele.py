def unique(arr):
    result = []

    for x in arr:
        if x not in result:
            result.append(x)

    return result


arr = [1, 2, 2, 3, 4, 4, 5]

print(unique(arr))
