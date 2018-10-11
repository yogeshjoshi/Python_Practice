if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sc = student_marks[query_name]
    avg = 0
    for s in sc:
        avg += s
    print("%.2f" % (avg/len(sc)))