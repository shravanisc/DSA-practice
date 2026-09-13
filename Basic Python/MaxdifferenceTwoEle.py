def maxdifference(n):
    lar=n[0]
    small=n[0]
    for i in n:
        if i>lar:
          lar=i
          
        if i<small:
           small=i
        
    diff=lar-small
    return diff
a=maxdifference([2,3,10,6,4,8,1])
print(a)