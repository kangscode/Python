A=10
B=5
print("type :",type(A<B));print("type :",(A<B))
num = 100;print("type : %s" % type(num))
flt = 321.321;print("type : %s" % type(flt))
ch = "A ";print("type : %s" % type(ch))
st = "test";print("type : %s" % type(st))

num = 100
print("type : %s\tid : %s" % (type(num),id(num)))
num = 321.321
print("type : %s\tid : %s" % (type(num),id(num)))
num = "A"
print("type : %s\tid : %s" % (type(num),id(num)))
num = "test"
print("type : %s\tid : %s" % (type(num),id(num)))

st1 = "Python"
st2 = "Test"
su = 100
flt = 1.11

num = '100'

print(flt+su)
print(st1 + st2)
#print(su+num)

su = 100

print('type(su) : ',type(su))
print('type(str(su)) : ',type(str(su)))
print('type(float(su)) : ',type(float(su)))
print('type(su) : ',type(su))


su = 100
num = '100'
flt = "1.111"
print(su+int(num))
print(su+float(flt))
print(str(su)+num)

# a = '백'
# print(int(a)) (x)

# print("숫자 입력")

# num1 = input()

# print("입력 받은 값:", num1)


# print("이름 입력")
# name = input()
# print("나이 입력")
# age = input()
# print(name,"님의 나이는",age,"살 입니다.")
# print("%s님의 나이는 %s살 입니다" % (name,age))
# print("%s님의 나이는 %s살 입니다" % (name,int(age)))

# print("두 수의 합을 구해 줍니다")
# print("두 수 입력")

# num1 = int(input())
# num2 = int(input())
# num3 = num1 + num2
# print("두 수의 합 ", num1,"+",num2,'=',num3)

# print("num1 type : ",type(num1))
# print("num2 type : ",type(num2))
# print("num3 type : ",type(num3))

# num1 = int(input())
# num2 = int(input())

# result = num1 + num2
# print(num1, "+", num2, "=", result)

# result = num1 - num2
# print(num1, "-", num2, "=", result)

# result = num1 * num2
# print(num1, "*", num2, "=", result)

# result = num1 / num2
# print(num1, "/", num2, "=", result)


# print("문자열 입력")
# name = input()
# print("정수 입력")
# age = int(input())
# print("실수 입력")
# flt = float(input())

# print("name 값: ",name,"\t type : ",type(name))
# print("age 값: ",age,"\t type : ",type(age))
# print("flt 값: ",flt,"\t type : ",type(flt))


# name = input("이름을 %d번입력 하세요 : " % 2)
# name = input(10.2)
# name = input("데이터를" "10개 입력")
# name = input("데이터를", "10개 입력")  (x)

# age = int(input("나이를 입력 하세요 : "))

# addr = input("주소를 입력 하세요 : ")

# print("이름 : ",name,"\n나이 : ",age,"\n주소 : ",addr)


# now_year = int(input("올해의 년도를 4자리로 입력하세요 "))
# birth_year = int(input("당신이 태어난 년도를 4자리로 입력하세요 "))
# old = now_year - birth_year + 1
# print("당신의 나이는 %d 살 입니다." % old)


# limit = 600
# weight1 = float(input("첫 번째 물건의 무게를 입력하세요."))
# weight2 = float(input("두 번째 물건의 무게를 입력하세요."))
# print("현재 엘리베이터에 허용무게는 %.2fkg입니다"
# % (limit-(weight1+weight2)))


height = float(input("키를 입력하세요 "))
standard = (height-100) * 0.9
print("표준체중은 %.2f 입니다." % standard)
weight = float(input("현재 체중을 입력하세요 "))
fat = (weight/standard)*100
print("표준체중은 %.2f 이고, 비만도는 %.2f 입니다"
% (standard, fat))









