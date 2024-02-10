# num = int(input("수 입력 : "))
# if num % 3 == 0:
#     if num % 2 == 0:
# # if num % 6 == 0:
#         print("num은 3의 배수면서 짝수 입니다")
# print("다음문장 실행")


# num = int(input("수 입력 : "))
# if num >= 0:
#     if num % 2 == 0:
#         print("num은 양의 짝수 입니다")
#     else:
#         print("num은 양의 홀수 입니다")
# else:
#     print("num은 음수 입니다")
# print("다음문장 실행")



# old_id = input("저장할 ID 입력: ")
# old_pw = input("저장할 PW 입력: ")
# print("인증 프로그램 입니다")
# print("ID와 PW를 입력하세요")
# new_id = input("ID 입력 : ")
# new_pw = input("비밀번호 입력: ")
# if old_id == new_id :
#     if old_pw == new_pw:
#         print("인증 통과")
#     else:
#         print("비밀번호가 틀렸습니다.")    
# else:
#     print("등록되지 않은 아이디 입니다.")

# old_id = input("저장할 ID 입력: ")
# old_pw= input("저장할 비밀번호 입력: ")
# print("인증 프로그램 입니다")
# print("ID와 PW를 입력하세요")
# new_id = input("ID 입력 : ")
# if old_id == new_id :
#     new_pw = input("비밀번호 입력: ")
#     if old_pw == new_pw:
#         print("인증 통과")
#     else:
#         print("비밀번호가 틀렸습니다.")    
# else:
#     print("등록되지 않은 아이디 입니다.")


# num = int(input("수 입력 : "))
# if num > 100:
#     print("100보다 큰 수 입력")
# elif num > 50:
#     print("50보다 큰 수 입력")
# elif num > 0:
#     print("0보다 큰 수 입력")
# else:
#     print("그 외의 값 입력")


name=input("이름 입력 : ")
hak=input("학번 입력 : ")
kor=int(input("국어점수 : "))
eng=int(input("영어점수 : "))
mat=int(input("수학점수 : "))
sum_=kor+eng+mat
avg=sum_/3
if avg >= 90: level='A'
elif avg >= 80 : level='B'
elif avg >= 70 : level='C'
elif avg >= 60 : level='D'
else : level='F' 
print("========================= 학생 정보 =========================")
print("이름\t학번\t국어\t영어\t수학\t총점\t평균\t학점")
print("%s\t%s\t%d\t%d\t%d\t%d\t%.2f\t%c"%(name,hak,kor,eng,mat,sum_,avg,level))


money=0
count=int(input("주문할 커피 수량 입력 : "))
if count > 10 :
    money=(2000*10)+(count-10)*1500
else :
    money=count*2000
print("주문한 커피의 총금액 : %d 원"%money)


num = int(input("정수 입력: "))    
if num == 0: print("0은 3의배수도 4의 배수도 아닙니다.")
elif num%3==0 and num%4==0: print("3의 배수이면서, 4의 배수입니다.")
elif num%3==0: print("3의 배수입니다.")
elif num%4==0: print("4의 배수입니다.")
else: print("3의 배수도, 4의 배수도 아닙니다.")


minute = int(input("비행기 탈 시간: "))
if minute<=0: print("요금: 30000")
else: print("요금:", 30000 + ((minute - 30)//10 + 1)*5000)

money=30000
time=int(input("비행기 탑승시간 입력 : "))
time-=30
if time > 0 :
    money=money+(time-1)//10*5000+5000
    # if  time %10 == 0:
    #     money=money+time//10*5000
    # else :
    #     money=money+time//10*5000+5000
print("비행기 탑승요금 : %d원"%money)
























