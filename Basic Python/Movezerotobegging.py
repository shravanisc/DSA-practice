def move(arr):
    result=[]
    for i in arr:
        if i == 0:
            result.insert(0,i)
        else:
            result.append(i)
    return result
arr=[1,0,2,3,0,3,4,5,0]
print(move(arr))