if __name__ == '__main__':
    students = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    #print(students)
    scores = set([students[x][1] for x in range(len(students))])
    #print(scores)
    scores = list(scores)
    #print(scores)
    scores.sort()
    #print(scores)
    students = [x[0] for x in students if x[1] == scores[1]]
    students.sort()
    #print(students)
    for s in students:
        print(s)