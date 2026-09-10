list=[1,2,3,4,5,34]
small=list[0]
small2=0
for i in list:

    if i<small:
        small2=small
        small=i
print(small2)