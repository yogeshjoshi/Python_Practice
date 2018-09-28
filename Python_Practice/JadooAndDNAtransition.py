r = ''
d = raw_input()
def change(d,r):
    for i in d:
        if i is 'G':
            r += 'C'
        elif i is 'C':
            r += 'G'
        elif i is 'T':
            r += 'A'
        elif i is 'A':
            r += 'U'
        else:
            print('Invalid Input')
            return 'f'
    return r

op = change(d.upper(),r)
if op != 'f':
    print(op)
        
#not efficent solution 
#can be reduced using Dicitionary
#in orignal this need to be done in 103 line