class Monster:
    def say(self):
        print("나는 몬스터다..")

goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다
a = 10
b = "문자열객체"
c = True

print(type(a))
print(type(b))
print(type(c))

# 문자열 객체안에 어떤 메서드가 있는지 확인하는 방법
print(b.__dir__())