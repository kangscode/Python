ls = [4,8,2,7,6]
for i in range(len(ls)-1): # 선택정렬할 때 기준이 되는 인덱스 지정. -1을 한 이유는 끝에는 비교대상이 없으므로
    for k in range(i+1, len(ls)): # 상위포문은 기준이 되고 종속 포문은 비교대상이 된다. 기준이 인덱싱이 증가할 때마다 비교대상의 i+1을 통해서 출발지도 하나뒤부터 시작하게 만들어준다.
        if ls[i]>ls[k]: # 이제 둘을 비교한다
            ls[i],ls[k] = ls[k],ls[i] #  기준이 비교대상보다 크면 자리를 스왑하게 된다.
print(ls)            


ls = [82,85,76,79,96]
rank = [1,1,1,1,1]
for i in range(len(ls)): #기준인덱스를 지정
    for k in range(len(ls)): # 비교대상의 인덱스를 지정
        if ls[i]<ls[k]: #기준인덱스와 비교인덱스를 비교해서 기준이 점수가 작으면 참
            rank[i] += 1 #기준의 점수가 작으면 rank를 하나씩 증가
for k in range (len(rank)) :
    print("점수: %d / %d등"%(ls[k],rank[k]))


ls = [10,20,30]
ls.append(1000)

for i in range(len(ls)):
    print("ls[{}] : {}".format(i,ls[i]))
print("리스트의 총 개수 : ",len(ls))
print("ls : ",ls)
ls=[]
print("ls초기화 후 : ",ls)


# ls = []
# for i in range(0 , 4) :
#     ls.append(0)
# Sum = 0

# for i in range(0 , len(ls)) :
#     ls[i] = int(input(str(i+1) + "번째 숫자 : "))
#     Sum += ls[i]

# for i in range(0 , len(ls)) :
#     print("입력 받은 값 ls[{}] : {}".format( i , ls[i] ))
# print("합 계 : %d " % Sum)


# num = int(input('몇개의 공간 만들겠습니까? :'))
# ls = []
# Sum = 0
# for i in range(num) :
#     ls.append(int(input(str(i+1) + "번째 숫자 : ")))
#     Sum += ls[i]

# for i in range(0 , len(ls)) :
#     print("입력 받은 값 ls[{}] : {}".format( i , ls[i] ))
# print("합 계 :", Sum)


List = [ 30 , 20 ,10 ]
print("현재 리스트 : " , List)

List.append(40)
print("append(40) 후 리스트 : " , List)

print("pop() 으로 추출한 값 : " , List.pop())
print("pop() 후 리스트 : " , List)
# test = List.pop(1)
# print(List)
# List.append(test)
# print(List)

List.sort()
print("sort() 후 리스트 : " , List)

List.reverse()
print("reverse() 후 리스트 : " , List)
del(List[2])
print("del() 후 리스트 : " , List)


List = [ 30 , 20 ,10 ]
print("현재 리스트 : " , List)

print(" 10 값의 위치 : " , List.index(10))

List.insert(2,200)
print("insert(2,200) 후 리스트 : " , List)

List.remove(200)
print("remove(200) 후 리스트 : " , List)

List.extend( [ 555 , 666 , 555 ] )
print("extend( [ 555 , 666 , 555 ] ) 후의 리스트 : " , List)

print("555 값의 개수 : " , List.count(555))


ls = [10,5,20,7,9,31,12,11,19,32]
odd=[]
even=[]
result=[]
for i in range(len(ls)):
    if i%2==0:
        odd.append(ls[i])
    else:
        even.append(ls[i])    
for i in range(len(odd)):
    result.append(even[i] - odd[i])
print("결과:", result)


ls = [10,5,20,7,9,31,12,11,19,32]
odd = 0
even = 0
for i in range(len(ls)):
    if i%2==0:
        even += ls[i]
    else:
        odd += ls[i]   
print("결과:", even - odd)


invertLs = []
ls = [10,5,20,7,9,31,12,11,19,32]
for i in range(1,len(ls)+1):
    invertLs.append(ls[-i])
print(invertLs)

import copy
ls = [10,5,20,7,9,31,12,11,19,32]
temp_ls = copy.deepcopy(ls)
invertLs = []
for i in range(len(ls)):
    invertLs.append(temp_ls.pop())
print(invertLs)    


ls = [10,5,20,7,9,31,12,11,19,32]
sortLs = ls[:]
for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if sortLs[i] > sortLs[j]:
            sortLs[i],sortLs[j] = sortLs[j],sortLs[i]
print(sortLs)

    
ls = [10,5,20,7,9,31,12,11,19,32]
reverseLs = ls[:]
for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if reverseLs[i] < reverseLs[j]:
            reverseLs[i],reverseLs[j] = reverseLs[j],reverseLs[i]
print(reverseLs)




















































