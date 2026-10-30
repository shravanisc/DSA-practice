


def reverse_string(str):
    length=len(str)
    result=""

    for i in range(length-1,-1,-1):
        result += str[i]
    return result


def palindrome(str1):
    a=reverse_string(str1)
    if str1 == a:
        return True
    else:
        return False

        
wordtocheck = input("Enter string to check: ")
# print(palindrome(wordtocheck))

isPalindrome = palindrome(wordtocheck)

if isPalindrome == True:
    print("Palindrome")
else:
    print("Not palindrome")



    def palindrome(text):
    rev = ""

    for ch in text:
        rev = ch + rev

    if text == rev:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome("madam")