list=[1,2,3,4,5,34]
lar=list[0]
lar2=0
for i in list:

    if i>lar:
        lar2=lar
        lar=i
print(lar2)