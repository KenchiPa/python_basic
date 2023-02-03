# 턱걸이 평균 측정 프로그램을 만들어보자. 먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다.
# 그리고 일주일간의 턱걸이 횟수를 입력 받아 리스트에 저장한다. 리스트에 저장된 데이터의 평균을 구해 출력한다.
# 표준입력: 1일차 턱걸이 횟수 >>> 20
#           2일차 턱걸이 횟수 >>> 23
#           3일차 턱걸이 횟수 >>> 16
#           4일차 턱걸이 횟수 >>> 14
#           5일차 턱걸이 횟수 >>> 24
#           6일차 턱걸이 횟수 >>> 27
#           7일차 턱걸이 횟수 >>> 30
# 표준출력: 22

data = []  # 빈 리스트 생성

x = int(input("1일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("2일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("3일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("4일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("5일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("6일차 턱걸이 횟수 >>>"))
data.append(x)
x = int(input("7일차 턱걸이 횟수 >>>"))
data.append(x)

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
avg = total / 7

print(int(avg))

# 반복문으로 변환 시
for i in range(1, 101):
    x = int(input(i, "일차 턱걸이 횟수 >>>"))
    data.append(x)