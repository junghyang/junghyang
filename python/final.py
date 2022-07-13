from ctypes import *
from test3 import move
from test3 import buff
from test3 import collect
from time import sleep
from random import randint

n = int(input("시행횟수 >> "))
dly = float(input("서버 딜레이 >> "))

print("3초후 시작")
sleep(3)

for i in range(n):
    if i%2: #짝수
        move(710,dly)
        buff(210,505,6,dly)
        collect(710)
    else: # 홀수
        move(712,dly)
        buff(210,505,6,dly)
        collect(712)