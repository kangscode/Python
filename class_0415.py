num1 = 10
num2 = 5
if num1 > num2:
    print("num1 이 num2보다 크다")


# num1 = int(input("수 입력 : "))
# if num1 % 2 == 0:
#     print("num1 : ",num1,"짝수다")
#     print("num1 : ",num1,"2의 배수이다")
# print("나는 다음 문장")


# print("1.easy game")
# print("2.hard game")
# print("3.exit")
# num1 = int(input("선택 : "))
# if num1 == 1:
#     print("easy game start")
# if num1 == 2:
#     print("hard game start")
# if num1 == 3:
#     print("game exit")


# day = int(input("날짜: "))
# if day%7 == 1:
#     print("월요일")
# if day%7 == 2:
#     print("화요일")
# if day%7 == 3:
#     print("수요일")
# if day%7 == 4:
#     print("목요일")
# if day%7 == 5:
#     print("금요일")
# if day%7 == 6:
#     print("토요일")
# if day%7 == 0:
#     print("일요일")


# number1 = int(input("첫번째 숫자 입력: "))
# if number1%3 == 0:
#     print("3의 배수입니다.")

# if number1>=0:
#     print("%d의 절댓값: %d" % (number1,number1))
# if number1<0:
#     print("%d의 절댓값: %d" % (number1,-number1))

# if number1%2 == 0:
#     print("짝수")
# if number1%2 == 1:
#     print("홀수")    

# number2 = int(input("두번째 숫자 입력: "))
# if number1>number2: 
#     print(number1)
# if number1<number2:
#     print(number2)

# number3 = int(input("세번째 숫자 입력: "))
# if number1>number2 and number1>number3:
#     print("number1")
# if number2>number1 and number2>number3:
#     print("number2")
# if number3>number1 and number3>number2:
#     print("number3")

# if number1>number2 and number1%2 == 0:
#     print("출력")
# if number1<number2 and number2%2 == 0:
#     print("출력")

# if (number1+number2)%2 == 0 and (number1+number)%3 == 0:
#     print("출력")


# num = int(input("수 입력 : "))
# if num == 1:
#     print("1입력")
# else:
#     print("1 이 아닌 값 입력")


# arr = [1,2,3,4,5]
#     #   [1,2,3,4,5]는 리스트라는 자료형이다~
#     #   리스트는 메모리에 연속적으로 데이터를 나열하는 자료형이다.
#     #   마치 c언어의 배열과 비슷하다고 생각하면 된다.  
# na = int(input("찾을 숫자 입력 : "))
#    # a in b ==> b안에 a가 존재 하면 참
#    # a not in b ===> b안에 a가 존재하지 않으면 참
#    # in을 멤버 연산자라 부른다. 반환되는 결과값은 True나 False로 반환된다.
# if na in arr:
#     print("arr : ",arr,"찾는 숫자가 존재 합니다 : ",na)
# else:
#     print("arr : ",arr,"안에는 찾고자 하는 숫자가 없습니다 : ",na)
# print('결과 : ',na in arr)


# st = "Hello Python Fun"
# na = input("찾고자 하는 문자열 입력 : ")
# if na in st:
#     print("st : ",st,"찾는 문자열 : ",na,"존재 한다")
# else:
#     print("st 안에는 ",na,"존재 하지 않습니다")


old_id = input("저장할 ID 입력 : ")
print("인증 프로그램 입니다")
print("ID와 PW를 입력하세요")
new_id = input("ID 입력 : ")
if old_id == new_id :
    print("인증 통과 했습니다")
else:
    print("인증 실패")

a=2
print(id(a)) # 모든 자료형을 객체로 관리(maybe) -String 상수풀










