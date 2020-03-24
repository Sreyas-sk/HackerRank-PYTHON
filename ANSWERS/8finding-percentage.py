if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
b=student_marks[query_name]
b=sum(b)
b=float(b/3)
print('%.2f'%b)

