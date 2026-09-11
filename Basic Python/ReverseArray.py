def reverse_array(arr):
    reverse=[]
    for i in range (len(arr)-1,-1,-1):
        reverse.append(arr[i])
    return reverse
arr=[11,22,33,44,55,66,77]
result=reverse_array(arr)
print(result)