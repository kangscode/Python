student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'}
print(student)

mobile = {"품명":"겔럭시","가격":100,"크기":10}
print(mobile)


impo = {}
impo['파이썬'] = 'www.python.org'
impo['네이버']='www.naver.com'
impo['구글']='www.google.com'

print("파이썬 : ",impo['파이썬'])
print("네이버 : ",impo['네이버'])
print("구글 : ",impo['구글'])
print(impo)


# impo = {}
# name = input('키값 입력 : ')
# val = input('값 입력')
# impo[name] = val

# print(name,": ",impo[name])


# overwatch={}
# for i in range(5):
#     name = input("케릭터명 입력: ")
#     skill = input("스킬명 입력: ")
#     overwatch[name] = skill
# print(overwatch)    


# import collections
# #순서있는 사전
# overWatch = collections.OrderedDict()
# i=0; name=""; val = ""
# for i in range(5):
#     name = input("이름(key) 입력 : ")
#     val = input("값(value) 입력 : ")
#     overWatch[name]=val
# print(overWatch)
# print(dict(overWatch))


num = { 1:"일" , 2:'이' , 3:'삼',4:"사"}

print('keys() 키: ' , num.keys())
print()
print('values() 값: ',num.values())


num = { 1:"일" , 2:'이' , 3:'삼',4:"사"}

print("num.keys() : ",num.keys())
print("list(num) : ",list(num)) #키 값만 리스트로 변환
print('list(num.keys()) : ' , list(num.keys()))
print()
print("num.values() : ",num.values())
print("list(num.values()) : ",list(num.values()))


# singer = {}
# singer['이름']=input("가수 이름 입력 : ")
# singer['구성원']=input("인원수 입력 : ")
# singer['대표곡']=input("대표곡 입력 : ")

# for i in singer.keys():
#     print('%s : %s' % (i,singer[i]))    


menu={};  bl = True;  num = 0
# while bl:
#     print("1.메뉴 등록"); print("2.메뉴별 가격 보기");  print("3.가격 수정");print("4.종료")
#     num=int(input(">>> "))
#     if num == 1:
#         name = input("메뉴 입력 : ") 
#         if menu.get(name) != None:
#             print("이미 등록된 메뉴입니다.")
#             continue
#         menu[name] = input("가격 입력 : ")
#     elif num == 2:
#         for i in menu.keys():
#             print(i,":",menu[i])
#     elif num == 3:
#         name = input("수정할 목록 입력")
#         if menu.get(name) == None:
#             print("존재하지 않는 메뉴입니다.")
#             continue
#         menu[name] = input("수정가격 : ")
#     elif num ==4:
#         print("프로그램 종료 합니다")
#         bl = False


# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}

# print(num)
# print("num.get(3) : ",num.get(3))
# print("num.get(9) : ",num.get(9))
# print("num.get(0) : ",num.get(0,'없음'))

# su = int(input("찾고자하는 키 입력 : "))
# if num.get(su) == None:
#     print("값이 없습니다")
# else:
#     print(num.get(su))


student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'}

print(student['학번'])
print(student['이름'])
print(student['학과'])
print()
print(list(student.items()))
print()
print(student)


name={ '이순신':"거북선",'세종대왕':'훈민정음','파이썬':'프로그래밍 언어'}
for key,value in name.items():
    print(key,":",value)

print("삭제 : ",name.clear())
print("삭제 후 값:",name)


num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}

print("변경전 값 : ",num)
print()
print("num.setdefault(9) : ",num.setdefault(9,"구~우"))
print()
print("변경전 후 : ",num)
print()
print("num.get(9)번째 value : ",num.get(9))


num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}
aaa={5:"오~", 6:"육",7:"칠",8:"팔"}
# print(num+aaa) +연산자 사용x

print("update 전 num : ",num)
num.update(aaa)

print("update 후 num : ",num)


num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"}

print("popitem() 전 num : %s\n" % num)

print("popitem 실행 결과 => ",end=" ")
print(num.popitem())
print("popitem() 후 num : %s\n" % num)

print("popitem 실행 결과 => ",end=" ")
print(num.popitem())
print("popitem() 후 num : %s" % num)


info={};  pe = []; bl = True;  num = 0
while bl:
    print("1.인적사항 등록"); print("2.검색");  print("3.종료")
    num=int(input(">>> "))
    if num == 1:
        pe.append(input("이름 입력 : ")); pe.append(input("점수 입력 : "))
        info[pe[0]] = pe[1]
    elif num == 2:
        name = input("찾고자하는 학생 이름 입력 : ")
        if info.get(name) == None:   print("찾고자 하는 학생이 없습니다")
        else:        print(name,"님 점수 : ",info.get(name))
    elif num ==3:
        print("프로그램 종료 합니다")
        bl = False
    pe.clear()
print(info)
print(pe)






















































