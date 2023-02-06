# 내장 모듈
# 파이썬 설치 시 자동으로 설치되는 모듈

import math

print(math.pi)
print(math.ceil(2.7))

from math import pi, ceil as c
print(pi)
print(c(2.7))

# 외부 모듈
# 다른 사람이 만든  파이썬 파일 pip로 설치해서 사용
# pyautogui: 마우스를 자동으로 움직이거나, 키보드를 입력하게 만드는 기능이 있는 모듈?
# $ pip install pyautogui
import pyautogui as pg

pg.moveTo(500, 500, duration=2)  # 마우스를 500,500 위치로 이동