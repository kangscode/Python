num = 100

print("정수 형 변수 사용: %d" % num)

print("정수 형 변수 사용:", num)

print("정수 형 변수 사용: num ")

num = 5

print("변경 전 num:", num)

num = num + 10

print("변경 후 num:", num)

num1 = 5
print("id num1:", id(num1))
num2 = 10
num1 = num1 + num2
print("id num1:", id(num1))
print(id(15))
# print("id num2:", id(num2))
# print("id num3:", id(sum_))

num1=10
num2=20
print("num1(%d) + num2(%d) = %d"  % (num1,num2, num1+num2))
print("num1(",num1,")+num2(",num2,")=",num1+num2)

num1=7
num2=5
plus = num1 + num2
minus = num1 - num2
mul = num1 * num2
div = num1 / num2
print("num1(%d) + num2(%d) = %d" % (num1,num2,plus))
print("num1(%d) + num2(%d) = %d" % (num1,num2,minus))
print("num1(%d) + num2(%d) = %d" % (num1,num2,mul))
print("num1(%d) + num2(%d) = %.2f" % (num1,num2,div))

python = 100
print("파이썬 %d점" % python)
age = 27
print("나는 %d살이다." % age)
python = 97
clang = 92
java = 95
sum_ = python + clang + java
avg = sum_ / 3
print("합계:", sum_)
print("평균: %.2f" % avg)

st = 11
time = 37
avg = time/st
print("한 정거장을 지나는데 걸리는 시간: %.2f분" % avg)

flt = 123.567
print(flt)
print(round(flt,-1))
print(flt)
print("round(flt):", round(flt))
print("round(flt,1)", round(flt,1))
print("round(flt,2) : " , round(flt,2))

one_fl = 500.23
to_fl = 14
av_fl = 260
to_height = av_fl * (to_fl-1) + one_fl
meter = to_height / 100
print("건물의 높이:", round(meter,3), "m")

sec=60*60 # 시간을 초로 환산
avg=sec/11.27 # 1시간에 11.27초가 몇번 들어가는지 계산
meter=avg*100 # 위에 행의 결과를 100m단위로 변환
kilo=meter/1000 # 위에 총이동거리는 m이므로 km로 변환
print("1시간 후 이동거리 : %.2fkm"%kilo)


flt = 123.123
print("%.3f + %.3f = %.3f" % (flt,321.321,flt+321.321))
print(flt,"+",321.321,"=",flt+321.321)

ch1,ch2 ,ch3= "파",'2',"썬"
print("%c + %c + %c = %s"%(ch1,ch2,ch3,ch1+ch2+ch3))
print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3)

str_1 = "python "; str_2 = "test"
str_3 = str_1 + str_2
print("%s + %s = %s" % (str_1,str_2,str_1+str_2))
print(str_1,"+",str_2,"=",str_1+str_2)












