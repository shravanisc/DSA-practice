def count_space(s):
    count=0
    for i in s:
        if i== " ":
            count+=1
    return count
out="hello world"
print(count_space(out))