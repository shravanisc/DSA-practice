def count_consonants(s):
    count = 0
    for i in s:
        if  i not in "aeiouAEIOU":
            count += 1
    return count

text = input("Enter a string: ")
print("Consonants:", count_consonants(text))
