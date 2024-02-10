# name = input("학생 이름: ")
# kor = int(input("국어 점수: "))
# eng = int(input("영어 점수: "))
# mat = int(input("수학 점수: "))
# total = kor + eng + mat
# avg = total / 3
# print("===================학생 정보===================")
# print("이름\t국어\t영어\t수학\t합계\t평균")
# print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,mat,total,avg))


num1 = 9; num2 = 2

print(num1 , " + " , num2 , " = " , num1 + num2)
print(num1 , " - " , num2 , " = " , num1 - num2)
print(num1 , " * " , num2 , " = " , num1 * num2)
print(num1 , " / " , num2 , " = " , num1 / num2)
print(num1 , " // " , num2 , " = " , num1 // num2)
print(num1 , " % " , num2 , " = " , num1 % num2)
print(num1 , " ** " , num2 , " = " , num1 ** num2)


su1=3.1; su2=3

print("su1 >= su2 : %s"%(su1 >= su2))
print("su1 <= su2 : %s"%(su1 <= su2))
print("su1 == su2 : %s"%(su1 == su2))
print("su1 != su2 : %s"%(su1 != su2))
print("su1 >= su2 : %d"%(su1 >= su2))
print("su1 <= su2 : %d"%(su1 <= su2))
print("su1 == su2 : %d"%(su1 == su2))
print("su1 != su2 : %d"%(su1 != su2))


su1 = su2 = 5
su1+=1
print("su1 + 1 = " ,su1)
su1-=1
print("su1 - 1 = ",su1)
su1*=su2
print("su1 * su2 = ",su1)
su1//=su2
print("su1 // su2 = ",su1)
su1%=su2
print("su1 % su2 = ",su1)


su1 = 5
su2 = 3
su1**=su2
su1-=2
print("su1 / 4 = ",su1 / 4)
print("su1 // 4 = ",su1 // 4)
print("su1 % 4 = ",su1 % 4)


print(0 or 0," : ",False or False)
print(1 or 0," : ",True or False)
print(0 or 1," : ",False or True)
print(1 or 1," : ",True or True)

print("not : ",not(0 or 0)," : ",not(False or False))
print("not : ",not(1 or 1)," : ",not(True or True))

print(0 and 0," : ",False and False)
print(1 and 0," : ",True and False)
print(0 and 1," : ",False and True)
print(1 and 1," : ",True and True)

print("not : ",not(0 and 0)," : ",not(False and False))
print("not : ",not(1 and 1)," : ",not(True and True))

# print(True and 30) - bool자료형과 정수 만나면 정수 출력
# and/or 논리연산자는 논리연산할 때는 인자로 받은 데이터값을 
# Boolean 값으로 바꿔서 계산하고, 결과값은 그 데이터값을 그대로 출력
a=20
b=10
print(False or (a+b))
print(True or (a+b))
print(False and (a+b))
print(True and (a+b))


num1 = 3
num2 = 5
result = num1 ^ num2
print(result)
result = num1 | num2
print(result)
print(~-10)
print(~11)
print(5<<2)
print(20>>2)




































