from ctypes import *
from re import A
from time import sleep
from time import time
from random import uniform
from random import randint
from test3 import collect
from test3 import type_key

path = "C:/Users/rlawo/Desktop/python/DD94687.64.dll"

d_dll = windll.LoadLibrary(path)

st = d_dll.DD_btn(0) #classdd 초기설정

DIR = 710

rad = randint(1,10)
DIR_a = 712
if DIR == 712:
        DIR_a = 710
    

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
