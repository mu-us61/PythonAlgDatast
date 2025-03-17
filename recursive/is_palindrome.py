# is palindrome

def isPalindrome(str):
    if len(str) in [1,0]:
        return True
    return str[0] == str[-1] and isPalindrome(str[1:-1])


print(isPalindrome("a"))
