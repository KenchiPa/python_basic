# 보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력해주는 프로그램을 작성해 보자.
# mystock.csv 파일로 부터 종목, 매입가, 수량, 목표가 정보를 가져온다
# 수익금 = (목표가 - 매입가) * 수량
# 수익률 = (목표가 / 매입가 - 1) * 100
# mystock.csv:
# 종목,매입가,수량,목표가
# 삼성전자,85000,10,90000
# NAVER,380000,5,400000
# 표준출력:
# 삼성전자 50000 5.88%
# NAVER 100000 5.26%

import csv

def show_profit(data):
    name = data[0]  # 종목
    purchase_price = int(data[1])  # 매입가
    amount = int(data[2])  # 수량
    target_price = int(data[3])  # 목표가

    profit = (target_price - purchase_price) * amount  # 수익금
    profit_ratio = (target_price / purchase_price - 1) * 100  # 수익률

    print(f"{name} {profit} {profit_ratio: .2f}")


# 파일 열기
file = open("./myvenv/Chapter10/mystock.csv", "r", encoding="utf8")

# 파일 데이터 읽기
reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)



file.close()