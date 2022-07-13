from ctypes import *
from re import A
from time import sleep
from time import time
from random import uniform
from random import randint


path = "C:/Users/rlawo/Desktop/python/DD94687.64.dll"

d_dll = windll.LoadLibrary(path)

st = d_dll.DD_btn(0) #classdd 초기설정

cooltime = 0
collect_time = time()

if st==1:
    print("OK")
else:
    print("Error")
    exit(101)

def type_key(key,dly_a,dly_b):
    d_dll.DD_key(key, 1)
    sleep(uniform(dly_a-0.03,dly_a+0.03))
    d_dll.DD_key(key, 2) 
    sleep(uniform(dly_b-0.03,dly_b+0.03))

def move(DIR,dly):
    rad = randint(1,10)
    start = time()
    type_key(503,0.1,0.15)
    type_key(504,0.05,0.05)
    type_key(402,0.10,0.05)
    type_key(503,0.1,0.05)
    #점숔 끝

    #숔캔 시작
    type_key(504,0.05,0.1)

    d_dll.DD_key(402, 1)#s
    sleep(uniform(0.02,0.08))
    if rad == 1:
        d_dll.DD_key(DIR, 1) #우측키 시작 #1
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(503, 2) 
        sleep(uniform(0.07,0.13))
    elif rad == 2:
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 1) #우측키 시작#2
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(503, 2) 
        sleep(uniform(0.07,0.13))
    elif rad == 3:
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 1) #우측키 시작#3
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(503, 2) 
        sleep(uniform(0.07,0.13))
    elif rad == 4:
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 1) #우측키 시작#4
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(503, 2) 
        sleep(uniform(0.07,0.13))
    elif rad == 5:
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(DIR, 1) #우측키 시작#5
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 2) 
        sleep(uniform(0.07,0.13))
    elif rad == 6:
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(503, 2)
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 1) #우측키 시작#6
        sleep(uniform(0.07,0.13))
    else:
        d_dll.DD_key(402, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(503, 1)#c
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(503, 2) 
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(DIR, 1) #우측키 시작#7
        sleep(uniform(0.02,0.08))

    type_key(504,0.05,0.1)      #숔캔 시작
    type_key(401,0.05,0.05)
    type_key(503,0.1,0.1)

    type_key(503,0.05,0.1)
    type_key(503,0.05,0.08)    

    type_key(504,0.05,0.05)
    type_key(401,0.05,0.05)
    type_key(503,0.05,0.1)
    type_key(504,0.05,0.1)
    type_key(401,0.05,0.3)
    type_key(503,0.1,0.1)

    if rad == 1:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 2)#1
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
    elif rad == 2:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 2)#2
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
    elif rad == 3:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 2)#3
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
    elif rad == 4:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(DIR, 2)
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
    elif rad == 5:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 2)#5
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
    elif rad == 6:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 2)#6
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
    elif rad == 7:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(DIR, 2)#7
        sleep(uniform(0.27,0.33))
    else:
        d_dll.DD_key(504, 1) #v 
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(504, 2)
        sleep(uniform(0.07,0.13))
        d_dll.DD_key(401, 1) #a
        sleep(uniform(0.02,0.08))
        d_dll.DD_key(401, 2) 
        sleep(uniform(0.27,0.33))
        d_dll.DD_key(DIR, 2)#8
        sleep(uniform(0.02,0.08))

    type_key(503,0.1,0.5)
    type_key(503,0.1,0.13)
    type_key(504,0.05,0.05)
    type_key(402,0.05,0.05)
    type_key(503,0.05,0.05)

    end = time()
    print(f"{dly-(end-start):.5f} sec")
    sleep(dly-(end-start))
    final = time()
    print(f"{final - start:.5f} sec")

def buff(time,buff_name,repeat,dly):
    global cooltime
    rad = randint(1,10)
    if cooltime >= time:
        cooltime = 0
        if rad >=7:
            for rep in range(repeat):
                type_key(buff_name,0.07,0.13)
        else:
            for rep in range(repeat+1):
                type_key(buff_name,0.05,0.1)
    else:
        cooltime=cooltime+dly
    print(buff_name,",",cooltime)

def collect(DIR):

    global collect_time
    rad = randint(1,10)
    collect_time_check = time()
    print(collect_time_check - collect_time)

    DIR_a = 712
    if DIR == 712:
        DIR_a = 710
    

        if collect_time_check - collect_time >= 100:
            collect_time = time()
            if rad > 7 :
                d_dll.DD_key(711, 1)
                sleep(uniform(0.1,0.13))
                d_dll.DD_key(503, 1)
                sleep(uniform(0.25,0.35))
                d_dll.DD_key(711, 2) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(DIR, 1) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(503, 2) 
                sleep(uniform(0.5,0.6))
            else :
                d_dll.DD_key(711, 1)
                sleep(uniform(0.13,0.16))
                d_dll.DD_key(503, 1)
                sleep(uniform(0.25,0.35))
                d_dll.DD_key(711, 2) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(503, 2) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(DIR, 1) 
                sleep(uniform(0.5,0.6))
            
            type_key(503,0.05,0.1)
            type_key(503,0.35,0.38) 

            type_key(503,0.05,0.1)
            type_key(503,0.35,0.38)   

            type_key(503,0.05,0.1)
            d_dll.DD_key(DIR, 2) 
            type_key(503,0.5,0.55)   

            d_dll.DD_key(709, 1)
            sleep(uniform(0.13,0.16))
            d_dll.DD_key(502, 1) 
            sleep(uniform(0.05,0.08))
            d_dll.DD_key(502, 2) 
            sleep(uniform(0.55,0.57))
            d_dll.DD_key(502, 1) 
            sleep(uniform(0.05,0.08))

            if rad > 3:
                d_dll.DD_key(709, 2) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(DIR_a, 1) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(502, 2) 
                sleep(uniform(0.52,0.55))
            else:
                d_dll.DD_key(709, 2) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(502, 2) 
                sleep(uniform(0.05,0.08))
                d_dll.DD_key(DIR_a, 1) 
                sleep(uniform(0.5,0.54))
            
        type_key(503,0.05,0.1)
        type_key(503,0.35,0.38) 

        type_key(503,0.05,0.1)
        type_key(503,0.20,0.23)
        type_key(504,0.05,0.05)
        type_key(401,0.05,0.05)
        type_key(503,0.05,0.1)   

        type_key(503,0.05,0.1)
        type_key(503,0.35,0.38) 
            
        type_key(503,0.05,0.1)
        type_key(503,0.35,0.38) 

        type_key(503,0.05,0.1)
        type_key(503,0.35,0.38) 
            
        type_key(503,0.05,0.1)
        d_dll.DD_key(DIR_a, 2) 
        type_key(503,0.8,0.85)  
            
        type_key(502,0.20,0.23)
        type_key(502,0.20,0.23)
        type_key(502,0.15,0.20)
        d_dll.DD_key(709, 1)
        sleep(uniform(0.05,0.08))
        type_key(502,0.3,0.35)
        d_dll.DD_key(709, 2)
        sleep(uniform(0.05,0.08))
