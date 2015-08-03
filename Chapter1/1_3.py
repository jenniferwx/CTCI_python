# Given two strings, write a method to decide if one is a permutation of the other

def isPermutation(string1, string2):
    if len(string1)!=len(string2):
        return False
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)
    return sorted_string1==sorted_string2

def isPermutation2(string1, string2):
    if len(string1) != len(string2):
        return False
    a = {}
    for ch in string1:
        if ch in a:
            a[ch] = a[ch]+1
        else:
            a[ch] = 1
    
    for ch in string2:   
        if ch not in a or a[ch]<=0:
            return False
        a[ch] = a[ch] - 1
    return True


if __name__ == '__main__':
    string1 = "abcdefg"
    string2 = "bcdefga"
    string3 = "abcddeg"
    string4 = "abcdx"

    print string1, ",", string2, isPermutation(string1, string2), isPermutation2(string1, string2)
    print string1, ",", string3, isPermutation(string1, string3), isPermutation2(string1, string3)
    print string1, ",", string4, isPermutation(string1, string4), isPermutation2(string1, string4)
    
