for i in range(1 , 11 , 1) :
           #(i=1, i<11, i+=1)
    print(i)

print('다음 문장')


for i in range(1 , 11 , 1) :
    if i %2 == 0:
        print("i = " , i , ": 값 확인")

print("다음 문장")

for i in range(0 , 11 , 2) :
    print("i = " , i , ": 값 확인")


for i in range(10, -1, -1):
            #(i=10, i>-1, i+=-1)   
    print(i, ": 10 ~ 0 까지 출력")


count = 0
for i in range(1, 11, 1):
    count += i
print("1~10까지의 합:", count)    


for i in range(1,11,1):
    print(i,end=" ")

print("다음 문장")

for i in range(1,31,1):
    print(i, end="\t")
    if i%5 == 0: print()


# i , Sum = 0 , 0
# start , en , grow = 0 , 0 , 0

# start = int(input("시작값 입력 : "))
# en = int(input("끝값 입력 : "))
# grow = int(input("증가값 입력 : "))

# for i in range ( start , en + 1 , grow ):
#     Sum = Sum + i

# print("%d에서 %d 까지 %d씩 증가한 값의 합 : %d"
#  % (start , en , grow , Sum))


for i in range(0,10):
    print(i)
print("------------------------------------------")
for i in range(10):
    print(i)
print("------------------------------------------")
for i in range(10,2):
    print(i)
print("------------------------------------------")
for i in range(0,10,2):
    print(i)
print("------------------------------------------")    


# start = int(input("시작값 입력 : "))
# end = int(input("끝값 입력 : "))
# grow = int(input("증가값 입력 : "))
# for i in range(start, end+1, grow):
#     if i%7 == 0:
#         print(i)

total = 0
for i in range(1,101):
    if i%3==0 and i%5==0:
        total += i
print(total)


# total = 0
# num1 = int(input("첫 번째 수: "))
# num2 = int(input("두 번째 수: "))
# if num1>num2:
#     imsi = num1
#     num1 = num2
#     num2 = imsi
# for i in range(num1,num2+1):
#     total += i
# print(total)    
    

num = 10
save = 10
for i in range(2,31):
    num *= 2
    save += num
print("30일째 입금액 : %d원" % num)
print("30일 후 총 저축액: %d원" % save)


for i in [1,2,3,4,5,6,7,8,9,10]:
    print("i: ",i)


st = "Hello Python"
for i in st:
    print("i:", i)





