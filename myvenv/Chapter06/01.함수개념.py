# 함수를 사용하는 이유

# 함수를 사용하지 않은 경우
print("안녕하세요. 켄치님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요. 켄치파파님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")

print("안녕하세요. 켄치마마님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

# 함수를 사용한 경우
def printMessage(name, date):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ", date, "일 남았습니다.")

printMessage("켄치", 30)
printMessage("켄치파파", 15)
printMessage("켄치마마", 7)