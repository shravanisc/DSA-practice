def remove_spaces(s):
    result = ""

    for i in s:
        if i!=" ":
            result += i

    return result


s = "Hello World Python"

print(remove_spaces(s))
