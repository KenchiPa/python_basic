# 주석 (comments)
# 1. 코드에 설명을 추가하고 싶을 때
# 2. 코드를 실행하고 싶지 않을 때

# 숫자 자료형
# 1. 정수형: 소수점이 없는 수
print(0)
print(1)
print(-1)

# 1개의 print문에서 여러개의 데이터를 출력하고 싶은 경우
# 자동으로 데이터 사이에 공백이 들어간다.
# 공백을 없애려면, sep="" 활용.
print(1, 2, 3, 0)
print(1, 2, 3, 0, sep="")

# 2. 실수형: 소수점이 있는 수
print(1.1)

# 문자열 자료형
# "" or '
# print문이 끝나면 한줄이 내려가는데 이어서 하기 위해서는 end='' 활용.
print("Hello", end="")
print('Kenchi')
print('"힘내자"라고 마음속에 다짐한다.')

# 불린형 자료형
# True or False
print(True)
print(False)