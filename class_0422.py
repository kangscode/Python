ls = [500, 200, 300, 400]; Sum = 0

print("ls:", ls)
print("ls[0]:", ls[0])
print("ls[1]:", ls[1])
print("ls[2]:", ls[2])
print("ls[3]:", ls[3])
print("ls[0]:", ls[-4])
print("ls[1]:", ls[-3])
print("ls[2]:", ls[-2])
print("ls[3]:", ls[-1])


# ls = [0 , 0 , "파이썬" , "쉽다"]; Sum = 0

# ls[0]=int(input("첫번째 숫자 입력 : "))
# ls[1]=int(input("두번째 숫자 입력 : "))
# ls[2]=int(input("세번째 숫자 입력 : "))
# ls[3]=int(input("네번째 숫자 입력 : "))

# Sum = ls[0] + ls[1] + ls[2] + ls[3]

# print("ls[0] :", ls[0])
# print("ls[1] :", ls[1])
# print("ls[2] :", ls[2])
# print("ls[3] :", ls[3])

# print("리스트의 합 : %d" % Sum)


# ls = [0 , 0 , 0 , 0]; Sum = 0

# print("len(ls) : ",len(ls))
# for i in range(len(ls)):
#     ls[i]=int(input(str(i)+"째 숫자 입력 : "))
#     Sum += ls[i]

# for i in range(len(ls)):
#     print("ls[%d] :"% i,ls[i])
# print("리스트의 합 :", Sum)


ls = [10 , 20 , 30 , 40]

print("ls : ",ls)

print("\nls[1:3] => ls[1] ~ [2] :",ls[1:3])
print("ls[0:3] => ls[0] ~ [2] :",ls[0:3])
print("ls[2:] => ls[2] ~ [끝까지] :",ls[2:])
print("ls[:2] => ls[0] ~ [1] :",ls[:2])


ls = [10 , 20 , 30 , 40]
arr = ls
arr[2] = 20000
print("ls : {} ls , id : {}".format(ls,id(ls)))
print("arr : {} arr , id : {}".format(arr,id(arr)))


ls = [10 , 20 , 30 , 40]
# arr = ls[:]
arr = [10 , 20 , 30 , 40]

# arr[2] = 20000

print("ls : {} ls , id : {}".format(ls,id(ls)))
print("arr : {} arr , id : {}".format(arr,id(arr)))


import copy
#import 모듈명 (표준함수를 불러)
ls = [10 , 20 , 30 , 40]
#arr = ls[:]
arr = copy.deepcopy(ls)
arr[2]='deepcopy'

print("ls : {} , ls id : {}".format(ls,id(ls)))
print("arr : {} , arr id : {}".format(arr,id(arr)))
print('=======================================')
print(ls==arr)

a= 2
b= 2
print(id(a))
print(id(b))


ls = [ 10 , 20 , 30 ]
arr = [ 40 , 50 , 60 ]

print("ls : " , ls)
print("arr : " , arr)

Str = ls + arr
print("ls + arr => Str : " , Str)

string = ls * 3
print("ls * 3 => string : " , string)


ls = [ 10 , 20 , 30 ]
arr = [ 40 , 50 , 60 ]

print("ls : " , ls)
print("arr : " , arr)

Str = [0,0,0]
string= [0,0,0]
for i in range(len(ls)):
    Str[i] = ls[i] + arr[i]
    string[i] = ls[i] * 3
print("ls + arr => Str : " , Str)
print("ls * 3 => string : " , string)
























