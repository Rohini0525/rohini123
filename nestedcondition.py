#find a largest of 3 numbers
num1=10
num2=12
num3=7
if num1>num2 and num1>num3:
    print("num1 is greater")
elif num2>num1 and num2>num3:
    print("num2 is greater")
else:
    print("num3 is greater")

#check a leap year
year=2024
if year%4==0 and year%100!=0 or year%400==0:
    print("year is a leap year")
else:
    print("year is not a leap year")

#Temperature check
temp=20
if temp<15:
    print("Cold")
elif temp>=15 and temp<=30:
    print("Warm")
else:
    print("Hot")

#Driving Eligibility
age=25
is_visiontest=True
is_drivingtest=False
is_documentation=True
if age>=18:
    if is_visiontest:
        if is_drivingtest:
            if is_documentation:
                print("verification successfuly done")
            else:
                print("invalid documents")
        else:
            print("requred driving test")
    else:
        print("required vision test")
else:
    print("age must be above 17 yrs")

#Vowel or consonant
char="E"
vowels="AEIOUaeiou"
if char in vowels:
     print("character is vowel")
else:
    print("character is consonant")

