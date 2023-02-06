import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형돈", 5, 32]
]

# 윈도우 운영체제에서는 자동으로 한줄 띄어주기 때문에 'newline=""'을 사용해 준다.
# encoding = "utf-8-sig" VSCode에서도 확인할 수 있게 해준다.
file = open("./myvenv/Chapter10/student.csv", "w", newline="", encoding = "utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()