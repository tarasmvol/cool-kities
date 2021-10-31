def isPalindrome(str):
    k = set(str)
    single_count = 0
    for i in k:
        if not str.count(i)%2:
            continue
        else:
            single_count +=1
    if single_count >=2:
        return False
    return True

#isPalindrome("ada")
#isPalindrome("qwertyuiu")
#isPalindrome("sdfsdfaagag")
#isPalindrome("trueistrue")
isPalindrome("abcab")
