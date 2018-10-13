

def split_and_join(line):
    # write your code here
    new_line = line.split(' ')
    ret_str  = '-'.join(new_line)
    return ret_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
