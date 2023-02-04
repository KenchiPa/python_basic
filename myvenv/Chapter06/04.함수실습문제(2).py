# 다음은 세개의 정수를 인자로 받아, 합계와 평균을 출력해주는 함수이다. 함수를 호출한 결과로 표준 출력이 나오도록 함수를 정의 해보자.
# def printSumAvg(x, y, z):
#     ???
#     ???
#     ???
# 함수호출:
# printSumAvg(10, 20, 30)
# 표준출력:
# 합계 : 60 평균 : 20

# 문자열 포매팅
def printSumAvg(x, y, z):
    """
    세개의 숫자를 받아 합계와 평균을 출력하는 함수
    """
    sum = x + y + z
    avg = sum / 3
    print(f"합계 : {sum} 평균 : {avg}")


printSumAvg(10, 20, 30)