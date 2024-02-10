# def sum_func(x1,x2,x3 = 100) : 
#     result = 0 
#     result =x1 + x2 + x3 
#     return result 
# def display(): 
#     Sum = 0 
#     a,b,c = 10 , 20 , 30 
#     Sum = sum_func(a , b) 
#     print("매개변수  2개  함수  호출  : " , Sum) 
#     Sum = sum_func(a ,b , c) 
#     print("매개변수  3개  함수  호출  : " , Sum) 
# display()


def sum_func(*par) : 
    result = 0 
    print("type : ",type(par)) 
    print("par : ",par) 
    for num in par : 
        result = result + num 
        print("num : %d" % num) 
    return result 
Sum = 0 
Sum = sum_func(10 , 20) 
print("매개변수  2개  함수  : %d" % Sum) 
Sum = sum_func(10 , 20 , 30 , 40) 
print("매개변수  4개  함수  : %d" % Sum)


def dic_func(**par) : 
    print("type(par):",type(par)) 
    for k in par.keys() : 
        print("{} : {} 명입니다".format(k , par[k]))
    print(par) 

dic_func(똭뚝뽹 = 123 , 꿔익꿔익 = 8 , test = '테스뚜')


def change(a,b,c): 
    return a+10,b+20,c+30 
    #c언어에서는 함수 종료시 return으로 함수 호출에 반환값을 하나만 전달 가능하다.
    #그런데 파이썬에서는 튜플이나 리스트와 같은 자료형으로 한번에 여러개를 반환 할 수 있다.

a,b,c=change(10,20,30) 
d = change(10,20,30) 
print("a,b,c :",a,b,c) 
print("d:{}, type{}".format(d,type(d)))


def swap(x,y): 
    return y,x 

a=10; b=20 
print("바꾸기  전  : ",a,b) 
a,b=swap(a,b) 
print("바꾼  후  : ",a,b)


swap = lambda a,b:[b,a] 
a=swap(10,20) 
print("swap 결과",a)


lam = lambda a:a*10 
hap = lambda a,b:a+b 
noData = lambda : print("인자값  없는  람다") 

print(lam(10)) 
print(hap(5,10)) 
print(noData())


# def startGame(): 
#     print("Game Start!!!!") 
# end = lambda :print("게임  종료")
# def test(): 
#     print("1.게임  시작") 
#     print("2.게임  종료") 
#     num = input("선택  : ") 
#     if num=="1": 
#         startGame() 
#     elif num=="2": 
#         end() 
# test()

import math

print(math.pi) 
print(math.factorial(5))   # 5!= 5x4x3x2x1 
print(math.sqrt(5)) 
print(math.log10(2))

from math import factorial, sqrt, pi

print(factorial(5)) 
print(sqrt(5)) 
# print(log10(2)) 사용x


from math import factorial, sqrt, pi 
import math 

print(factorial(5)) 
print(sqrt(5)) 
print(math.log10(2)) 
print(math.log10(3)) 
print(math.gcd(12,18)) #최대공약수


import statistics 
points = [65, 75, 55] 
print('평균 : ', statistics.mean(points)) 
print('분산 : ', statistics.variance(points)) 
print('표준편차 : ', statistics.stdev(points)) 
#----------------------------------------- 
import statistics as st 
points = [65, 75, 55] 
print('평균 : ', st.mean(points)) 
print('분산 : ', st.variance(points)) 
print('표준편차 : ', st.stdev(points))


import calcula3tor as cal 
from calcula3tor import info 

print("1인치 : %.2fcm"%cal.inch) 
print("1~10까지의 누적합:",cal.calc_sum(10)) 

info() 
info() 
info()


n1= 10 
n2=0 
try: 
    result=n1/n2 
    print("%d / %d = %d" %(n1,n2,result)) 
except: 
    print("0으로 나눌 수 없습니다.") 
    print("프로그램 정상 종료!!")


# while True:
#     try  : 
#         n1= int(input("정수1: ")) 
#         n2= int(input("정수2: ")) 
#         break 
#     except: 
#         print("숫자로만 입력하세요")   
#         # print("%d / %d = %d” %(n1,n2,result")) 
# try: 
#         result=n1/n2 
#         print("%d / %d = %d" %(n1,n2,result)) 
# except: 
#         print("0으로 나눌 수 없습니다.") 
# print("프로그램 정상 종료!!")


# s = input("정수: ") 
# try : 
#     point = int(s) 
#     print(150 /point) 
# except ValueError: 
#     print("숫자로만 입력하세요~") 
# except ZeroDivisionError: 
#     print("0으로 나눌 수 없습니다.") 
# except: 
#     print("알수 없는 오류 발생. 점검 후 조치하겠습니다..") 
# print("프로그램 정상 종료" )


pet = ['거북이', '타란튤라','전갈']
for i in range(4):
    try:
        print(pet[i],'키울래용!')
    except:
        print('애완동물의 정보가 없습니다.')
    finally:#예외처리(에러)와 상관없이 꼭 실행되야 하는경우
        print('애완동물 넘 조아~~')
print('프로그램 정상 종료!')


import random

i=0 
for i in range(5): 
    print(i," ",random.random())


import random 
i=0 
for i in range(5): 
    print(i," ",random.randrange(1,10))




















































