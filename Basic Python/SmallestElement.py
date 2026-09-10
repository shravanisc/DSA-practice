def smallest(n):
    small=n[0]
    for i in n:
        if i<small:
            small=i
    return small
a=[87,22,33,45,7,2]
output=smallest(a)
print(output)