# 로또에 당첨 되서 퇴사를 하고 싶었던 김로또는 로또 예상번호 추출 프로그램을 파이썬으로 작성하려고 한다.
# 다음 조건에 따라 김로또의 프로그램을 완성해보자.
# 1. 로또 번호 6개를 생성한다.
# 2. 로또 번호는 1 ~ 45 까지의 랜덤한 번호다.
# 3. 6개의 숫자 모두 달라야 한다.
# 4. getRandomNumber() 함수를 사용해서 구현한다.(random 모듈의 sample 함수는 사용하지 않는다.)
# 표준출력:
# 1 8 11 13 26 42

#  3번 조건이 포함되지 않은 생성기(중복)
import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = []  # 로또 번호를 저장할 리스트

for i in range(6):
    random_number = get_random_number()
    lotto_num.append(random_number)

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")

#  중복제거한 로또 생성기
import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_num = []  # 로또 번호를 저장할 리스트

count = 0  # 현재 뽑은 숫자 개수

while True:
    if count > 5:
        break
    random_number = get_random_number()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count += 1
    

lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")    