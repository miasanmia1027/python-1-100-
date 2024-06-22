#31번
N=int(input())

값=[]


for l in range(N):
    q,w,e=map(int,input().split())

    if q==w==e:
        result=10000+q*1000
    elif q==w :
        result=1000+q*100
    elif q==e :
        result=1000+q*100
    elif e==w :
        result=1000+e*100
    elif q!=w!=e:
        result=max([q,w,e])*100
        
    값.append(result)
    
최고값=max(값)

print(최고값)
#32번
a=input()

if a=="A+":
    print(4.3)
elif a=="A0":
    print(4.0)
elif a=="A-":
    print(3.7)
elif a=="B+":
    print(3.3)
elif a=="B0":
    print(3.0)
elif a=="B-":
    print(2.7)
elif a=="C+":
    print(2.3)
elif a=="C0":
    print(2.0)
elif a=="C-":
    print(1.7)
elif a=="D+":
    print(1.3)
elif a=="D0":
    print(1.0)
elif a=="D-":
    print(0.7)
elif a=="F":
    print(0.0)
#33번
H,M=map(int,input().split())

if M-45>=0:
    print(H,M-45)
elif M-45<0 and H-1>=0:
    print(H-1,M+60-45)
elif M-45<0 and H-1<0:
    print(23,M+60-45)
#34번
#너무 어려월서 선배의 도움받음
#35번
n=int(input())

R=[]

for l in range(n):
    r,e,c=map(int,input().split())
    
    if r>e-c:
        reault="do not advertise"
    elif r==e-c:
        reault="does not matter"
    else:
        reault="advertise"
    
    R.append(reault)
    
for g in R:
    print(g)
    
#36번
V=int(input())

a=input()

if V==len(a):
    a=list(a)
    result_a=result_B=0
    for l in a:
        if l=="A":
            result_a+=1
            
        if l=="B":
            result_B+= -1
            
    
    
    if result_a>0:
        print("B")
    elif result_B<0:
        print("A")
    elif result_a==result_B:
        print("Tie")
        
    


#37번
N=int(input())

g=[]

if N%2!=0:
    for l in range(N):
        a=input()
        g.append(a)
        

R=0
for n in range(len(g)):
    if n==1:
        result=1
    if n== 0:
        result=-1  
    R += result    

if R>0:
    print( "Junhee is not cute!")
elif R<0:
    print("Junhee is cute!")
#38번
R=input()

if R== ''.join(reversed(R)):
    print("1")
else:
    print("0")
#39번
값=[]

while True:
    result=""
    x,y=map(int,input().split())
    
    if y!=0:
        if x%y!=0 and x/y<1:
            result="factor"
        elif x%y==0 and x/y>1:
            result="multiple"
        elif x%y!=0:
            result="neither"
    if x == 0 and y == 0:
        break
    
    값.append(result)


for g in 값:
    print(g)

#40번
result = 0
K=[]
while True:
    
    M,F=map(int,input().split())
    if M==0 and F==0:
        break
    
    result = M+F
    K.append(result)
    
for l in K:
    print(l)



