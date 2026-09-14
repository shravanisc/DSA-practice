def max(arr):
    max_value=arr[0]
    max_index=0

    for i in range (len(arr)):
        if arr[i]>max_value:
            max_value = arr[i]
            max_index = i

    return max_value, max_index


arr = [10, 25, 7, 40, 15]

print(max(arr))