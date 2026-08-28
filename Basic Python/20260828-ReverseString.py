def reverse_using_slicing(n):
    return n[::-1]

def reverse_using_loop(str):
    length = len(str)

    outputString = ""

    for i in range(length-1, -1, -1):
        outputString += str[i]

    return outputString
        



a=reverse_using_slicing("python programming")

print(reverse_using_loop("python programming"))




print(a)
def reverse_another_string(string):
    reversed_text = ""
    for char in string:
        reversed_text = char + reversed_text 
    return reversed_text
print(reverse_another_string("shravani"))