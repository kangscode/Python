aa=[[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
print('[0][0]',aa[0][0])
print('[0][1]',aa[0][1])
print('[0][2]',aa[0][2])
print('[0][3]',aa[0][3])
print('[1][0]',aa[1][0])
print('[1][1]',aa[1][1])

for i in range(len(aa)):
    for k in range(len(aa[i])):
        print("[%d][%d]"% (i,k), aa[i][k], end='\t')
    print()
for i in aa:
    for k in i:
        print(k, end='\t')
    print()    


aa=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
a = aa[0] #얕은 복사
a[1]=20000

print('[0]',aa[0])
print(a)
print(aa)


import copy
aa=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
#a = aa[0][:]
a = copy.deepcopy(aa[0])
a[1]=200000000

print('[0]',aa[0])
print(a)
print(aa)


aa=[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]
a = aa[:][:] #얕은 복사로 됨(전체 복사할 때)
# a = copy.deepcopy(aa[0])
a[0][1]=200

print('[0]',aa[0])
print(a)
print(aa)


ls_2 = []
value = 1
for k in range(3):
    ls_1 = []
    for i in range(4):
        ls_1.append(value)
        value += 1
    ls_2.append(ls_1)
for i in ls_2:
    for k in i:
        print(k, end='\t')
    print()


be = ['2019','12','31']
print(be)

af=list(map(int,be))
print(af)


tp = (10,20,30)
print("tp : ",tp)
print("tp type : ",type(tp))
print("tp len : ",len(tp))


tp1 = 10,20,30
print("tp1 : ",tp1)
print("tp1 type : ",type(tp1))

print("tp1[0] type : ",type(tp1[0]))

# tp1[0] = 100 #값 변경x


tpInt = (10)
print("tpInt : ",type(tpInt)) #<class ‘int’>
# print(tpInt[0]) 튜플x

tpT1 = (10,)
print("tpT1 : ",type(tpT1)) #<class ‘tuple’>

tpT2 = 10,
print("tpT2 : ",type(tpT2)) #<class ‘tuple’>
print(tpT2[0])


tt1 = ( 10 , 20 , 30 , 40 )
tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3]
print("튜플 합 : %d" % tt2)

print("tt1[1:3] : " , tt1[1:3])
print("tt1[1:] : " , tt1[1:])
print("tt1[:3] : " , tt1[:3])


a = 1,2,3
b = 4,5,6
c = a+b

print("a : ",a)
print("b : ",b)
print("c : ",c)


pack = 1,2,"패킹"
print("packing\npack : ",pack)

a,b,c = pack
print("unpacking\na:",a,"b:",b,"c:",c)


tp = 100,200,"함수",100,'개수'

print("tp안의 200의 위치 : " ,tp.index(200),"번째 인덱스")
print("tp안의 100의 개수 : ",tp.count(100)," 개")




















































































