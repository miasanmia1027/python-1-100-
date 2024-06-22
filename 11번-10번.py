#11번
N,M=map(int,input().split())


if 1 <= N<=300 and 1 <= M<=300:
    print(N*M-1)
#12번
T=int(input())

if T==5:
    a_1,b_1=map(int,input().split())
    a_2,b_2=map(int,input().split())
    a_3,b_3=map(int,input().split())
    a_4,b_4=map(int,input().split())
    a_5,b_5=map(int,input().split())

    
    print("Case #1: ",a_1+b_1)
    print("Case #2: ",a_2+b_2)
    print("Case #3: ",a_3+b_3)
    print("Case #4: ",a_4+b_4)
    print("Case #5: ",a_5+b_5)
#13번

T=int(input())

if T==5:
    a_1,b_1=map(int,input().split())
    a_2,b_2=map(int,input().split())
    a_3,b_3=map(int,input().split())
    a_4,b_4=map(int,input().split())
    a_5,b_5=map(int,input().split())

    
    print("Case #1: 1+1=",a_1+b_1)
    print("Case #2: 2+3=",a_2+b_2)
    print("Case #3: 3+4=",a_3+b_3)
    print("Case #4: 9+8=",a_4+b_4)
    print("Case #5: 5+2=",a_5+b_5)
#14번

import datetime
print(datetime.date.today())
#15번
print("12")
print("ahndonggeon")
#16번
A,B=map(int,input().split())
C=int(input())

C_hour=C//60
C_minute=C%60

A_hour=A+C_hour+(B+C_minute)//60
B_minute=(B+C_minute)%60

x=' '
if 0<=A<=59 and 0<=B<=59 and 0<=C<=1000:

    print(A_hour, x, B_minute)
#17번
A,B,C=map(int,input().split())
D=int(input())


if 0<=A<=23 and 0<=B<=59 and 0<=C<=59 and 0<=D<=5000000:
    hour=int((D//60)//60)
    minute=int((D//60)%60)
    second=int(D%60)

    hour_last=int((((second+C)//60+minute+B)//60+hour+A)%24)
    minute_last=int(((second+C)//60+minute+B)%60)
    second_last=int((second+C)%60)


print(hour_last,minute_last,second_last)
#18번
A,I=map(int,input().split())

if 1<=A<=100 and 1<I<=100:
    print(A*(I-1)+1)
elif 1<=A<=100 and I==1:
    print(A*I)
#19번
T=int(input())

x,y,z=input().split()
x=float(x)
x_round=round(x,1)


if T!=0:
    if y=="@":
        x_1=x*3
    elif y=="%":
        x_1=x+5
    elif y=="#":
        x_1=x-7
   



    if z=="@":
        x_2=x_1*3
    elif z=="%":    
        x_2=x_1+5
    elif z=="#":
        x_2=x_1-7
    T_1=T-1       





q,w,e,r=input().split()
q=float(q)
q_round=round(q,1)


if T!=0:
    if w=="@":
        q_1=q*3 
    elif w=="%":
        q_1=q+5
    elif w=="#":    
        q_1=q-7


    if e=="@":
        q_2=q_1*3
    elif e=="%":    
        q_2=q_1+5
    elif e=="#":    
        q_2=q_1-7


    if r=="@":  
        q_3=q_2*3
    elif r=="%":    
        q_3=q_2+5
    elif r=="#":    
        q_3=q_2-7
    T_2=T_1-1





a,s=input().split()
a=float(a)
a_round=round(a,1)


if T!=0:
    if s=="@":  
        a_1=a*3
    elif s=="%":    
        a_1=a+5
    elif s=="#":
        a_1=a-7
    T_3=T_2-1







print("{:.2f}".format(x_2))
print("{:.2f}".format(q_3))
print("{:.2f}".format(a_1))
#20번
T=int(input())

if 1<=T<=1000:
    results=[]
    while T!=0:
        if T!=0:
            q,w=input().split()
            if 1<=len(w)<=20:
                q=int(q)
                w_1=list(w)
       
                result=""
                for 곱하기 in w_1:
                    result += 곱하기*q
        
            results.append(result)  
            T -= 1


    for 반복 in results:
        print(반복)
#20번
A=int(input())
a=input()
B=int(input())

if a=="*":
    print(A*B)
elif a=="+":
    print(A+B)














