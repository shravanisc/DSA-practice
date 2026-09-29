def first_non_repeat(s):
    for i in s:
        if s.count(i) == 1:
            return i
           
print(first_non_repeat("swiss"))

def first_nonrepeating(s):
    feq={}
    for i in s:
        feq[i]= feq.get(i,0)+1
    for i in s:
        if feq[i] == 1:
         return i

print(first_nonrepeating("helloh"))
 

