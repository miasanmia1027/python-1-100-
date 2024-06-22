#1번hello world
print("Hello World!")
#2번 a+b
A,B=map(int,input().split())

if A>0 and B<10:
    print(A+B)
#3번
A,B=map(int,input().split())

if A>0 and B<10:
    print(A*B)
#4번
A,B=m
map(int,input().split())

if A>0 and B<10:
    print(A/B)
#5번
A,B=map(int,input().split())

if 1 <= A<= 10000 and 1 <= B <= 10000:
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)

#6번
A,B,C=map(int,input().split())

if 2 <= A <= 10000 and 2 <= B <= 10000 and 2 <= C <= 10000:
    print((A+B)%C)
    print( ((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)
    
#7번
A=int(input())
B=int(input())
if 0 < A and B < 10:
    print(A+B)
#8번
a=int(input())
b=input()


B=list(b)
B_1=int(B[2])
B_2=int(B[1])
B_3=int(B[0])
B_5=int(b)


print(a*B_1)
print(a*B_2)
print(a*B_3)
print(a*B_5)
#10번
R1,S=map(int,input().split())


if -1000<= R1<=1000 and -1000<= S <=1000:
    print(S*2-R1)





