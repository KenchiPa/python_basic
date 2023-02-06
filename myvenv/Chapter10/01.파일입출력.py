# 1. 파일 쓰기
file = open("./myvenv/Chapter10/data.txt", "w", encoding = "utf8")  # 파일명과 확장자만 입력 시 루트 폴더에 생성된다.
file.write("1. 켄치와 함께 파이썬 공부")
file.close()

# 2. 파일 추가
file = open("./myvenv/Chapter10/data.txt", "a", encoding = "utf8")
file.write("\n2. 열심히 해보자")
file.close()

# 3. 파일 읽기
file = open("./myvenv/Chapter10/data.txt", "r", encoding = "utf8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end = "")
    if data == "":
        break
file.close() 

