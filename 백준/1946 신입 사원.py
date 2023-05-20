import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        new = set()  # 신입사원으로 뽑힐 사람 set
        N = int(input())
        grades = []
        for _ in range(N):
            grades.append(list(map(int, input().split())))  # 서류, 인터뷰 성적 입력
        grades.sort(key=lambda x: x[0])

        person = grades[0]
        count = 1
        for i in range(1, len(grades)):
            if grades[i][1] < person[1]:
                person = grades[i]
                count += 1

        print(count)
