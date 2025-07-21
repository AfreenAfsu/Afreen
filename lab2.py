#1
def div(a,b):
    result=a/b
    print("Division result",result)
div(10,2)    

#2
check_number=lambda x:"Positive" if x>0 else("Negative" if x<0 else "Zero")
print(check_number(20))
print(check_number(-10))
print(check_number(0))

#3
name=input("Enter your name")
print("Name in lowercase",name.lower())

#4
import random
numbers = [random.randint(1, 100) for _ in range(5)]
print("Numbers", numbers)
print("Maximum number", max(numbers))
print("Minimum number", min(numbers))

#5 
def square(num):
    return num*num
number=4
result=square(number)
print("Square of",number,"is",result)

