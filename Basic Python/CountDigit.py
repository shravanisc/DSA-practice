def count_digits(s):
    count=0
    for i in s:
        if i.isdigit():
            count+=1
    return count
s= "hello123dffi"
print(count_digits(s))