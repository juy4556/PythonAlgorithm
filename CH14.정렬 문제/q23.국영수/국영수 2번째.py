import sys
input = sys.stdin.readline

n = int(input())
student_info = []

for _ in range(n):
    student_info.append(list(input().split()))

student_info.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(student_info)):
    print(student_info[i][0])