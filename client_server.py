8.1

n = int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print('sum =',sum)

8.2

n = int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i**2
print(‘amount of degrees=’, sum)

8.3

n = int(input())
m = int(input())
sum=0
for i in range(n,m+1):
    sum=sum+i
print('sum =',sum,',','average =',sum/(m+1-n))

8.4

n = int(input())
sum=0
for i in range(n+1):
    if i%2==0:
        print('even ',i)
8.5

for i in range(12):
    if i!=3 and i!=6:
     print(i, end=' ')

8.6

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('"*333**555*"')
    elif i % 5 == 0:
        print('"*555*')
    elif i % 3 == 0:
        print('"*333*"')
    else:
        print(i)

8.7

n = int(input('Количество дней '))
x = int(input('Обьем горшка '))
y = int(input('Сколько сьел '))
gorst1 = 0
sum_bochka=0
day=0
for i in range(n):
 sum_bochka+=x
 court=y*i
 gorst1+=y*i
 day+=1
 if court >= x:
  print('остаток в бочке', sum_bochka-gorst1)
  # print('сьел', gorst1,'горстей')
  print('c',day+1,'дня горшочек будет пустым')
  break

8.8

a = int(input())
i = 1
while i < a:
    a = a / 2
if a == 1:
    print('power of two')
else:
    print('no')

8.9

a = int(input())
b=0
for i in range(2,a):
    if a%i==0:
        b+=i
if b%2==0 or a==0:
    print('love')
else:
    print('not love')

8.10

d = int(input())
b=0
for i in range(d):
    b+=1
    if b==1:
       a='kaktus geran fialka'
    if b==2:
       a='fialka kaktus geran'
    if b==3:
        a = 'geran fialka kaktus '
        b=0
    if i==d-1:
     print(a)

8.11

f = int(input())
b=1
for i in range(1,f+1):
   b=b*i
print(b)

