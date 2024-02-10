# result,temp = 0,0
# result = int(input("수 입력 : "))
# while True:
#     temp = int(result%10)
#     result = int(result/10)
#     print(temp,end="")
#     if not result: break
# print("\n프로그램 종료")


# def reverseCode(): 
#     result,temp = 0,0 
#     result = int(input("수  입력  : ")) 
#     while True: 
#         temp = int(result%10) 
#         result = int(result/10) 
#         print(temp,end="") 
#         if not result: break
# print("프로그램  시작") 
# reverseCode() 
# print("\n프로그램  종료")


# def sel_machine(): 
#     sel = 0 
#     sel = int(input("음료  선택\n1.콜라\n2.핫6\n3.포카리\n입력  : ")) 
#     if sel == 1 :   print('콜라  등장') 
#     if sel == 2 : print('핫6 등장') 
#     elif sel == 3 : print('포카리  등장') 
#     else :  print('만들어  드세요^^') 

#     if sel >=1 and sel <=3: 
#         print("맛있게  드세요^^") 
# sel_machine()


# def calc(): 
#     result=0 
#     su1,op,su2 = int(input("숫자: ")),input("부호: "),int(input("숫자: "))   
#     if op=='+':
#         result = su1+su2 
#     if op=='-':
#         result = su1-su2 
#     elif op=='*':
#         result = su1*su2
#     elif op=='/':
#         result = su1/su2 
#     print(su1,op,su2,'=',result)
# calc()


# def cal(su1,op,su2): 
#     result=0

#     result = su1+su2 
#     print(su1,'+',su2,'=',result) 

# su1,op,su2 = int(input("숫자:")),input("부호  :"),int(input("숫자:")) 
# cal(su1,op,su2)    


# def cal(su1,op,su2): 
#     result=0 
#     result = su1+su2 
#     print('cal 실행') 
#     return result 

# su1,op,su2 = int(input("숫자:")),input("부호  :"),int(input("숫자:"))   
# result=cal(su1,op,su2) 
# print(su1,'+',su2,'=',result) 
# print("다음  문장  실행")


def showAvrg(a,b,c): 
    print("{}와  {}의  평균".format(a,b)) 
    print("값은  {}입니다".format(round(c,1))) 
def avrg(j,k): 
    total=j+k
    f=total/2 
    return f
i=2; j=3; 
f=avrg(i,j) 
showAvrg(i,j,f) 
print("다음  문장  실행")


def func2(a,b): 
    a+=5; b*=10 
    print("func2 : a={}, b={} ".format(a,b)) 
def func1(): 
    a=5;b=10 
    func2(a,b) 
    print("func1 : a={}, b={}".format(a,b)) 
func1()


# def hol_jjak(num1):
#     return num1%2
# num1=int(input("정수입력 : "))
# ret = hol_jjak(num1)
# if ret :
#      print("%d는 홀수다"%num1)
# else : 
#      print("%d는 짝수다"%num1)


# def Three_func():
#     num1=int(input("정수입력 : "))
#     if num1 %3 == 0 : print("%d는 3의 배수이다"%num1)
# Three_func()


# def output_Data(num1,op,num2,ret):
#     print(num1,op,num2,"=",ret)   

# def calc(num1,op,num2):
#     if op == '+' :ret = num1+num2
#     elif op == '-' :ret = num1-num2
#     elif op == '*' :ret = num1*num2
#     elif op == '/' :ret = num1/num2
#     output_Data(num1,op,num2,ret)

# def input_Data():
#     num1=int(input("정수1 입력 : "))
#     op  = input("부호 입력 : ")
#     num2=int(input("정수2 입력 : "))
#     calc(num1,op,num2)


def reverseCode(num1):
    temp = 0
    reverse=0
    while True:
        temp = num1%10                 
        reverse*=10
        reverse+=temp
        num1 = num1//10        
        if not num1: break            
    return reverse
num1=int(input("정수 입력 : "))
ret=reverseCode(num1)
print("결과 :",ret )


def funca() : 
    a=100  #지역 변수
    print("func1의  a : %d" % a) 
def funcb() : 
    a=200  #지역 변수
    print("func2의  a : %d" % a) 
funca() 
funcb()


def func3() : 
    print("func1의  a : %d" % a) 

def func4() : 
    print("func2의  a : %d" % a) 

a =200 #전역  변수 

func3() 
func4()


def func5() : 
    a = 123 
    print("func1의  a : %d" % a) 
    print(id(a))
    
def func6() : 
    print("func2의  a : %d" % a) 
    print(id(a))
a =200 #전역  변수 
func5() 
func6()
print(id(a))


def func7() : 
    global a 
    a = 1222 
    print("func1의  a : %d" % a) 
def func8() : 
    print("func2의  a : %d" % a) 
a =200 #전역  변수 
func7() 
func8()
























































