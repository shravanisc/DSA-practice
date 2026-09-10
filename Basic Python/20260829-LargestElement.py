def large_element(list):
    largest=list[0]
    for i in list:
        if i > largest:
            largest = i

    return largest



# list =  [4,5,8,6,3,7,1]

# largest=list[0]

# for i in list:
#     if i > largest:
#         largest = i

# print(largest , "is largest number") 


myList = [4, 11, 5, 9, 3, 6, 7]
outputLargestNumber = large_element(myList)


print("the largest number in list is ", outputLargestNumber)