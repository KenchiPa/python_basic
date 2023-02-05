# 상속
# 클래스들에 중복된 코드를 제거하고 유지보수를 
# 편하게 하기 위해서 사용한다.

# 개선사항
# 드래곤 클래스에 인스턴스 속성으로 3개의 스킬을 추가하자.
# 드래곤이 스킬을 쓰면 속성 중에 하나가 무작위로 사용된다.

# 클래스 변수
# 인스턴스들이 모두 공유하는 변수

import random

# 부모 클래스
class Monster:
    max_num = 1000

    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1  # 클래스 변수 self 사용하지 않는다
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass

class Shark(Monster):
    def move(self):  # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("불뿜기", "꼬리치기", "날개치기")

    def move(self):  # 메서드 오버라이딩
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")

wolf = Wolf("울프", 1500, 200)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크", 3000, 400)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 8000, 800)
dragon.move()
dragon.skill()
print(dragon.max_num)
