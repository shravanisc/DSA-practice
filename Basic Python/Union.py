def union(arr1, arr2):
    result = []

    for x in arr1:
        if x not in result:
            result.append(x)

    for x in arr2:
        if x not in result:
            result.append(x)

    return result


a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(union(a, b))
