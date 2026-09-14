def min(arr):
    min_value=arr[0]
    min_index=0
    for i in range(len(arr)):
        if arr[i]<min_value:
            min_value=arr[i]
            min_index=i
    return min_value,min_index
arr=[10,25,7,40,15]
print(min(arr))