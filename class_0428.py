Str = 'Have a nice day'
for i in range(len(Str)):
    print("Str[%d]:" % i, Str[i], end='')
print()
for i in Str:
    print(i,end="")
print()
print("문자열의 총 길이:",len(Str))
print("Str:", Str)


Str = 'Have a nice day'

arr = Str[7:11]
print("Str : " ,Str)
print("arr : " , arr)


Str = "즐거운 파이썬"
print("Str\t: " , Str)
print("Str[0]\t: " , Str[0])
print("Str[1:3] : " , Str[1:3])
print("Str[3: ] : " , Str[3 : ])
print("Str[ : 3] : " , Str[ : 3])


Str = 'Have a'
print("변경 전 Str : ",Str)

Str+=' nice day'

print("변경 후 Str : " , Str)
print("Str * 3 : ",Str*3)


Str = 'Pythone is Easy. 그리고 programming 할만하다 ^^'
print("Str : ",Str)
print()
print('Str.upper() : ',Str.upper()) #소문자를 대문자로 변경
print()
print('Str.lower() : ',Str.lower()) #대문자를 소문자로 변경
print()
print('Str.swapcase() : ',Str.swapcase()) #대소문자 상호 변경
print()
print('Str.title() : ',Str.title()) #각 단어의 첫번째 문자 대문자로 변경


st = 'NevEr -eVer110gIVeup'

st=st.title()

print(st)


st = 'Have a nice day'
print("st : ",st)
print()
print("st안에 'a'문자 개수 : ",st.count('a'))
print("st안에 'day'문자열 개수 : ",st.count('day'))
print("st안에 'dak'문자열 개수 : ",st.count('dak'))


st = "It is a fun Python class"

print("총 개수 : ",len(st))
print("a 개수:",st.count('a'))
print("s 개수:",st.count('s'))


st = 'Have a nice day'
print("st : ",st)

print("find: 'day'위치 : ",st.find('day'))
print("index: 'day'위치 : ",st.index('day'))
print("find: 'kkk'위치 : ",st.find('kkk'))
# print("index: 'kkk'위치 : ",st.index('kkk')) 오류 발생


st = 'Have a nice day'
print("st : ",st)

print("find: 'day'위치 : ",st.find('a'))
print("find: 'day'위치 : ",st.find('a',2))
print("find: 'day'위치 : ",st.find('a',6))
print("find: 'day'위치 : ",st.find('a',14))


st = 'Have a nice day Have a nice day Have a nice day'
print(st.count('a'))
result = []
i=0
while True:
    if st.find('a',i) == -1: break
    result.append(st.find('a',i))
    i = st.find('a',i) + 1
print(result) 


st = ' 파 이 썬 '

print('st\t\t:{}{}{}'.format('*',st,'*'))
print()
print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))


st = '파이썬파'

print('st\t\t:' ,st)
print()
print('Str.strip("파")\t:', st.strip('파'))
print("========================================")

st = '파이썬'
print('st\t\t:' ,st)
print()
print('Str.strip("파")\t:', st.strip('파'))


st = '---파---이---썬---'
print('st\t\t:',st)
print('st.strip("-")\t:',st.strip('-'))

print('st.rstrip("-")\t:',st.rstrip('-'))

print('st.lstrip("-")\t:',st.lstrip('-'))


st = '2015/04/02 2015/04/02 2015/04/02'

print('st\t\t:',st)
print('replace()\t:',st.replace('/','.'))
print('replace([0:4])\t:',st.replace(st[0:4],'2017'))


st = """
오늘 하루도 즐겁게
오늘 하루도 행복하게
오늘 하루도 최선을
"""

print(st)


st = """ 
김개똥  -2017년  03월  24일 
홍길동구리  -2015년  04월  02일 
선우선녀  -2018년  05월14일 
"""
st = st.replace('-',':')
i=0
while True :
    i=st.find('년',i)
    if i != -1 :
        st=st.replace(st[i-4:i],'1999')
        i+=1
    else:
        break
print(st)

a=True
while a:
    print("안녕")
    a=False
else:
    print("??")

a = 3, c=4
b= 4
print(a)
print(b)






























