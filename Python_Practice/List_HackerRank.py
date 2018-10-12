if __name__ == '__main__':
    N = int(input())
    list = []
    while N >0:
        x = input().split(' ')
        instruction = x[0]
        if instruction == 'insert':
            list.insert(int(x[1]),int(x[2]))
        elif instruction == 'remove':
            list.remove(int(x[1]))
        elif instruction == 'append':
            list.append(int(x[1]))
        elif instruction == 'pop':
            if len(list) != 0:
                list.pop()
        elif instruction == 'sort':
            list.sort()
        elif instruction == 'reverse':
            list.reverse()
        elif instruction == 'print':
            print(list)
        N-=1
                