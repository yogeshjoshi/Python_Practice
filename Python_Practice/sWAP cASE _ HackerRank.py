def swap_case(s):
    list = []
    for i in range(len(s)):
        if (s[i].islower()):
            list.append(s[i].upper())
        elif(s[i].isupper()):
            list.append(s[i].lower())
        else:
            list.append(s[i])
    return ''.join(list)
