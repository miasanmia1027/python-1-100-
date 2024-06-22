#21번
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
#22번
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
#23번
A=int(input())
a=input()
B=int(input())

if a=="*":
    print(A*B)
elif a=="+":
    print(A+B)
#24번
r=int(input())

if 90<=r<=100:
    print("A")
elif 80<=r<=89:
    print("B")
elif 70<=r<=79:
    print("C")
elif 60<=r<=69:
    print("D")
else:
    print("F")
#25번
A,B,C = map(int,input().split())
if 1<=A<=100 and 1<=B<=100 and 1<=C<=100:
    if A<=B<=C or C<=B<=C:
        print(B)
    elif B<=A<=C or C<=A<=B:
        print(A)
    elif A<=C<=B or B<=C<=A:
        print(C)
#27번
N=int(input())
num=2
G=[]
while True:
    if N%num==0:    
        N /= num
        G.append(num)
        continue
    
    if N%num!=0:
        num +=1

    if N==1:
        break

for l in G:
    print(l)
        
#28번
S=int(input())
num=0
R=0
G=[]
while S>=R:
    num+=1
    R+=num

    G.append(R)
    
K=max(G)

len_G=len(G)

print(len_G-1)
  
#29번
R_R=[]

while True:
    x,y=map(int,input().split())
    
    if x<=y:
        result="No"
    elif x>y:
        result="Yes"
    if x==0 and y==0:
        break
    R_R.append(result)
    
for l in R_R:
    print(l)
##30번
q,w=map(int,input().split())
a,s=map(int,input().split())
z,x=map(int,input().split())


if q==a:
    result=z
elif q==z:
    result=a
elif a==z:
    result=q



if w==s:
    result_1=x
elif w==x:
    result_1=s
elif s==x:
    result_1=w


print(result,result_1)



















