def first_non_repeat(s):
    for i in s:
        if s.count(i) == 1:
            return i
           
print(first_non_repeat("swiss"))