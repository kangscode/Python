st = 'Never ever give up'

print('st\t\t: ' , st)
print('st.split()\t: ',st.split())


st = '하나:둘:셋'

print('st\t\t: ' , st)

print('st.split(:)\t: ',st.split(':'))

st = '일,이,삼'
print('st.split(,)\t: ',st.split(','))


st = 'Never ever give up'
print('st : ',st)
print('st.splitlines(): ',st.splitlines())
st = '''
Never ever give up
Never ever give up
'''
print('st.splitlines(): ',st.split('\n'))
st = "하나\n둘셋"
print('st.splitlines(): ',st.splitlines())


Str = '123'
print('"%".join(123)\t: ','%'.join(Str))
print('123.join("%a")\t: ',Str.join('%a'))

li=['','123','456']
print('"공백".join([123,456])\t: '," ".join(li))
li=['','안녕하세요','만나서 반갑습니다','행복한 하루 되세요^^']
print('"엔터".join(li)\t: ',"\n\n".join(li))


Str = 'python'

print('Str\t\t: ',Str)

print('Str.center(10)\t: ',Str.center(10))
print('Str.center(10,"-"): ',Str.center(10,'-'))

print('Str.ljust(10)\t: ',Str.ljust(10),Str.ljust(10,"="))

print('Str.rjust(10)\t: ',Str.rjust(10),Str.rjust(10,'-'))

print('Str.zfill(10)\t: ',Str.zfill(10))


accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
a = accountBook.split(',')
for i in range(len(a)):
    b = a[i].split()
    for i in range(3):
        if i==2: print('$', end='')
        print(b[i], end='\t')
    print()
   
accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000" 
replaceAB = accountBook.split(',')#,기준으로  리스트로  저장 
k=0 
for i in replaceAB: 
    replaceAB[k]=i.lstrip() #각  문자열의  왼쪽  공백  삭제  후  저장(_coffee,_food,_dress) 
    k+=1 
kk='$ ' # 공백과 달러 사이
print('item'.ljust(10),end='') 
print('date'.ljust(10),end='') 
print('$(price)'.ljust(10)) 
for i in range(len(replaceAB)): 
    z=replaceAB[i].split() #공백을  기준으로  리스트로  저장 
    for k in range(len(z)): 
        if k == 0 : 
            print(z[k].ljust(10),end="") #10칸  확보후  왼쪽  출력 
        elif k ==1 : 
            print(z[k].ljust(10),end="") #10칸  확보후  왼쪽  출력 
        elif k == 2 : 
            print("{:,}".format(int(z[k])).join(kk).ljust(10)) 


Str = 'python te12st 1234'

print("Str.isdigit() : ",Str.isdigit())#숫자로만 구성
print("Str[9:11].isdigit() : ",Str[9:11].isdigit())#숫자로만 구성

print("Str.isalpha() : ",Str.isalpha())#글자로 구성
print("Str[:6].isalpha() : ",Str[:6].isalpha())#글자로 구성

print("Str.isalnum() : ",Str.isalnum())#글자 + 숫자
print("Str[7:13].isalnum() : ",Str[7:13].isalnum())#글자 + 숫자

print("Str.islower() : ",Str.islower())#소문자
print("Str.isupper() : ",Str.isupper())#대문자
print("Str.isspace() : ",Str.isspace())#공백


info = """ 
jo 9abc08-3022023 
cho 900402-1011232 
test 1234567-1234567 
lee 980908-3a2b0c3 
kim 900514-2022023 
"""
# a=info.split()
# print(a)
# i=1
# while i<len(a):
#     lo = a[i].find('-')
#     if len(a[i][:lo])==6 and a[i][:lo].isdigit()==True:
#         if len(a[i][lo:])==7 and a[i][lo:].isdigit()==True:
#             a[i] = a[i].replace(a[i][8:],'*******')
#     i += 2
# print(' '.join(a))



lo=0
while True:
    lo = info.find('-',lo)
    if lo == -1: break
    if info[lo+1:lo+8].isdigit() and not info[lo-7:lo].isdigit() and info[lo-6:lo].isdigit():
        info=info.replace(info[lo+1:lo+8],'*******')
    lo+=1
print(info)        

    















































































