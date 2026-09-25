def frequency_of_char(str,str1):
    if len(str)!=len(str1):
        return False
    count={}
    count1={}
    for i in str:
       count[i]=count.get(i,0)+1
    print(count)
    for i in str1:
        count1[i]=count1.get(i,0)+1
    print(count1)
    for i in str:
        if count[i] != count1[i]:
          return False
    return True
a="cat"
b="tac"
print(frequency_of_char(a,b))
    