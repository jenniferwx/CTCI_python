def isUnique(string):
    if len(string)>256:
        return False
    a = [0]*256
    for ch in string:
        if a[ord(ch)]:
            return False
        a[ord(ch)] = 1 
    return True


def isUnique2(string):
    a = {}
    if len(string)>256:
        return False
    for ch in string:
        if ch in a:
            return False
        a[ch] = True
    return True

if __name__ == '__main__':
    string = 'abcdefg'
    string2 = 'abcdefga'
    string3 = ''
    print string, isUnique(string), isUnique2(string)
    print string2, isUnique(string2), isUnique2(string2) 
    print string3, isUnique(string3), isUnique2(string2) 
