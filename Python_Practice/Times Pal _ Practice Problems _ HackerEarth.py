t = int(input())
while t>0:
    str1 = input()
    str2 = input()
    counter = 0
    for i in range(len(str1)+1):
        new_str = str1[:i]+str2+str1[i:]
        if new_str == new_str[::-1]:
            counter+=1
    t-=1
    print(counter)
