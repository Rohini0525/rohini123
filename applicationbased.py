#Electricity bill calculation
usage=105
if usage<=100:
    bill=usage*5
    print(f"Electricity bill is {bill}")
elif usage>100 and usage<=200:
        bill=usage*10
        print(f"Electricity bill is {bill}")
else:
      bill=usage*15
      print(f"Electricity bill is {bill}")

#Season finder
month="January"
if month=="December" or month=="January" or month=="February":
    print("season is winter")
elif month=="March" or month=="April" or month=="May":
    print("season is Spring")
elif month=="June" or month=="July" or month=="August":
     print("season is summer")
else:
     print("season is Auntumn")

#categorize BMI
BMI=25
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<25:
    print("Normal")  
elif BMI>=25 and BMI<30:
    print("Overweight")
else: 
     print("Obese")
           
               
#Character type checking
Name="@#"
if Name>="A" and Name<="z":
     print("Alphabets")
elif Name>="0" and Name<="9":
     print("digits")
else:
     print("special character")

#Password validation
PW="biomed123"
size=len(PW)
if size>=8:
    if "@" in "biomed123":
        print("strong password")
    else:
        print("required @ in the password")
else:
     print("required atleast 8 characters")


    
     