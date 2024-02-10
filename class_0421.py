# i=1
# while True:
#     print(i, "종속 문장",end=" ")
# i+=1


i=1
flag = True
while flag:
    print(i, "종속 문장",end=" ")
    if i == 10:
        flag = False
    i+=1


i=0
while True:
    if i == 3:
        print("3출력")
        break
    print(i,"출력")
    i+=1

print("다음 문장")


i=0
while i<5:
    i+=1
    if i == 3:
        print("3출력")
        continue
    print(i,"출력")
print("다음 문장")    


# num,result,i = 0,0,1
# flag = True
# while flag:
#     num = int(input("1~10사이의 숫자 입력: "))
#     if num<1 or num>10:
#         print("잘못 입력 다시")
#         continue
#     else: 
#         flag = False
# else:
#     print("next...")
# while i<=num:
#     result += i; i+=1
# else:
#     print("1~",num,"까지의 합:",result)    


for i in range(0,3,1):
    for k in range(0,5,1):
        if k == 3:
            break
        print("(i: %d\tk: %d)" % (i,k))
print()

i=0
while i<3:
    k=0
    while k<5:
        if k==3:
            break
        print("(i: %d\tk: %d)" % (i,k))
        k+=1
    i+=1


total = 100000
rat = 2
day = 1
while True:
    total = total - rat*20
    if day%10 == 0:
        rat *= 2
    if total<=0:
        break
    day += 1 
print("며칠:", day,"\t쥐의 수:", rat)       



print("요금을 투입하세요")
money = int(input("> "))
while True:
    print("{:=^50}".format("커피 자판기"))
    print("1. 커피<200>", end='\t')
    print("2. 코코아<250>", end='\t')
    print("3. 종료")
    print("선택하신 메뉴의 번호를 입력하세요")
    num = int(input("> "))
    if num==1: 
        if money<200: 
            print("돈이 부족합니다.")
            break
        print("커피 주문완료")
        money -= 200
    elif num==2: 
        if money<250: 
            print("돈이 부족합니다.")
            break       
        print("코코아 주문완료")
        money -= 250
    elif num==3: 
        print("잔돈을 반환합니다.")
        break
print("잔돈:", money)

























