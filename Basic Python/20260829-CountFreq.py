def count_frequency(list):
    feq={}
    for i in list:
        feq[i]=feq.get(i,0)+1
    return feq
a=[11,23,34,11,22,12,11]
print(count_frequency(a))







# list=[1,2,3,3,2,1,23,1]
# feq={}
# for i in list:
#     feq[i]=feq.get(i,0)+1
# print(feq)

