def count(sen):
    words=sen.split()
    return len(words)
sen=input("enter sentence")
print("number of words",count(sen))