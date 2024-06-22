#41번
n=int(input())
Q1=Q2=Q3=Q4=축=0
for q in range(n):
    x,y=map(int,input().split())
    if x>0 and y>0:
        Q1 +=1
    elif x<0 and y>0:
        Q2 +=1
    elif x<0 and y<0:
        Q3 +=1
    elif x>0 and y<0:
        Q4 +=1
    else :
        축 += 1
        
print("Q1:", Q1)
print("Q2:", Q2)
print("Q3:", Q3)
print("Q4:", Q4)
print("AXIS:", 축)
#42번
#하성이 형이 가르쳐줌
#43번
#이것도 하성이형이 알려줌
#44번
A=60*5
B=60
C=10


T=int(input())

A_result=T//A
B_result=(T%A)//B
C_resilt=((T%A)%B)//C
if T%C!=0:
    print("-1")
else:
    print(A_result,B_result,C_resilt)
#45번
n = int(input())

chang = 100
shang = 100

for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        chang -= b
    elif a > b:
        shang -= a

print(chang)
print(shang)
#46번
n = int(input())

chang = 100
shang = 100

for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        chang -= b
    elif a > b:
        shang -= a

print(chang)
print(shang)
#47번
T = int(input())

for 안동건 in range(T):

    g = 9

    result_a_list = []
    result_b_list = []

    while g != 0:
        result_a, result_b = input().split()
        result_a_list.append(result_a)
        result_b_list.append(result_b)
        g -= 1



    for i in range(len(result_a_list)):
        result_a_list[i] = int(result_a_list[i])

    for i in range(len(result_b_list)):
        result_b_list[i] = int(result_b_list[i])

    result_1=1
    result_2=1
    result_3=1
    result_4=1
    result_5=1
    result_6=1
    result_7=1
    result_8=1
    result_9=1





    if result_a_list[0]<result_b_list[0]:
        result_1=1
    if result_a_list[1]<result_b_list[1]:
        result_2=1
    if result_a_list[2]<result_b_list[2]:
        result_3=1
    if result_a_list[3]<result_b_list[3]:
        result_4=1
    if result_a_list[4]<result_b_list[4]:
        result_5=1
    if result_a_list[5]<result_b_list[5]:
        result_6=1
    if result_a_list[6]<result_b_list[6]:
        result_7=1
    if result_a_list[7]<result_b_list[7]:
        result_8=1
    if result_a_list[8]<result_b_list[8]:
        result_9=1


    if result_a_list[0]>result_b_list[0]:
        result_1=-1
    if result_a_list[1]>result_b_list[1]:
        result_2=-1
    if result_a_list[2]>result_b_list[2]:
        result_3=-1
    if result_a_list[3]>result_b_list[3]:
        result_4=-1
    if result_a_list[4]>result_b_list[4]:
        result_5=-1
    if result_a_list[5]>result_b_list[5]:
        result_6=-1
    if result_a_list[6]>result_b_list[6]:
        result_7=-1
    if result_a_list[7]>result_b_list[7]:
        result_8=-1
    if result_a_list[8]>result_b_list[8]:
        result_9=-1


    real_result=result_1+result_2+result_3+result_4+result_5+result_6+result_7+result_8+result_9

    if real_result>0:
        print("Yonsei")
    elif real_result<0:
        print("Korea")
    else :
        print("Draw")

    #48번
#하성이 형이 도아줌
#49번
A,B = map(int,input().split())


if 0<A<10**10000 and 0<B<10**10000:
    print(A+B)
#번호 하나를 빼먹음
    
        