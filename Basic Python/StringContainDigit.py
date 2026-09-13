def digits(s):
    for i in s:
        if i< '0' or i> '9':
            return False
    return True
print(digits("123453hee"))   