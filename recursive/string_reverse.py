

# string reverse recursive

def reverse(str):
    if len(str)==0:
        return ""
    return reverse(str[1:]) + str[0]

print(reverse("abc"))
