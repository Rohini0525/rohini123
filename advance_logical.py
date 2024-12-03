#Triangle validation
s1=2
s2=3
s3=4
scnt=3
sum=s1+s2
if scnt==3:
    if sum>s3:
        print("its a triangle")
    else:
        print("not trianle")
else:
    print("required 3 sides for triangle")

#Calculating tax based on salary
salary=450000
if salary>1000000:
    tax=(salary*20)/100
    print(f"tax is {tax}")
elif salary>500000 and salary<=1000000:
    tax=(salary*10)/100
    print(f"tax is {tax}")
elif salary<=500000:
    tax=(salary*5)/100
    print(f"tax is {tax}")

#Catogarize age
age=45
if age>=0 and age<=12:
    print("you are a child")
elif age>=13 and age<=19:
    print("you are a teen ager")
elif age>=20 and age<=59:
    print("you are an adult")
elif age>=60:
    print("you are a senior")

#AND operator-num>10 and divisible by 2
num=15
if num>10 and num%2==0:
    num=bool(num)
    print(num)
else:
    print(not num)

#Or operator-num<5,num>20
num=4
if num<5 or num>10:
    num=bool(num)
    print(num)
else:
    print(not num)