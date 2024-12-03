#1.fruits with index
fruits="apple","banana","cherry"
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

#2.iterative over string
letter="rohini"
for ch in letter:
    print(ch)

#3.iterative over range
for i in range(5):
    print(i)

#4.Using range()with start,stop, step
for num in range(1, 5, 3):
    print(num)

#5.Iterating over a dictionary
person={"name":"xyz","age":25,"city":"pune"}
for key, value in person.items():
    print(f"{key}:{value}")

#6.using for with else
for i in range(5):
    print(i)
else:
    print("loop finished")


#7.Breaking loop
for num in range(10):
    if num==5:
        print("breaking loop")
        break
    print(num)

#8.skipping iteration with continue
for num in range(5):
    if num==2:
        continue
    print(num)

#9.iterating with enumerate
animals=["dog","cat","rabbit"]
for index, animal in enumerate(animals):
    print(f"{index}:{animal}")

#10.sum of numbers in a list
numbers=[1,2,3,4,5]
total=0
for num in numbers:
    total+=num
    print(f"sum:{total}")
    
#11.find even odd numbaer
for num in range(1,11):
    if num%2==0:
        print(f"{num}:even number")
    else:
        print(f"{num}:odd number")