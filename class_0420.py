st = "It is a fun Python class"
count = 0
count_a = 0
count_s = 0
for i in st:
    count += 1
    if i=="a": count_a += 1
    if i=="s": count_s += 1
print("총 개수:", count)
print("a 개수:", count_a)
print("s 개수:", count_s)


print("{0}+{1}={2}".format(10,2,10+2))
print("{2}+{1}={0}".format(10,2,10+2))
print("{}+{}={}".format(10,2,10+2))

print("{:,}".format(1000000)) # 정수 자릿수 콤마 표시

print("{0:<10},왼쪽정렬,{1:0<10}".format('첫번째','두번째'))
print("{:>10},오른쪽정렬,{:9>10}".format('첫번째','두번째'))
print("{:^10},가운데정렬,{:5^10}".format('첫번째','두번째'))

print("I eat {} apples". format(3))

print("{:d}".format(100))
print("{:.2f}".format(100.12344554343))


for i in range ( 0 , 3 , 1):
    for k in range ( 0 , 5 , 1):
        print("이중 for 문 (i : %d\tk : %d)" % (i , k ))


print("{:-^61}".format(' 구 구 단 '))
for i in range(2,10):
    print("{:^5}".format('%d단'%i),end="\t")
print()
print("-"*64)
for i in range(1,10,1):
    for k in range(2,10,1):
        print("%d*%d=%d"%(k,i,k*i), end='\t')
        # print("{}*{}={}".format(k,i,k*i), end="\t")
    print()
    

for i in range(0,5,1):
    print("상위포문",i,"일때 하위 포문: ", end='')
    for k in range(0,5,1):
        print("%3d"% (k*i), end=' ')
    print()    
        

i=0
while i<5:
    print(i, "종속 문장")
    i+=1

print("다음 문장")

for i in range(0,5,1):
    print(i,"종속 문장")


i=0
while i<5:
    print(i, "종속 문장")
    i += 1
else:
    print("조건식이 거짓일 경우:", i)
print("다음 문장")















