#1
num=int(input("Enter a number:"))
if num%2==0:
   print("The number is Even.")
else:
  print("The number is Odd.")

#2
marks=[]
for i in range(5):
  mark=float(input(f"Enter marks for subject{i+1}:"))
  marks.append(mark)
average=sum(marks)/5
if average>=90:
    grade='A'
elif average>=80:
    grade='B'
elif average>=70:
    grade='C'
elif average>=60:
    grade='D'
else:
    grade='F'
print("\Average Marks",average)
print("Grade",grade)


#3
principal=200
rate=5
time=5
simple_interest=(principal*rate*time)/100
print("Simple Interest is",simple_interest)


#4
km=float(input("Enter distence in kilometers"))
conversion_factor=0.621371
miles=km*conversion_factor
print("Distence in miles",miles)


#5
num=int(input("Enter a number"))
is_prime=True
if num<=1:
    is_prime=False
else:
    for i in range(2,num):
      if num %i==0:
         is_prime=False
         break
if is_prime:
    print("Prime number")
else:
   print("Not a prime number")


#6
student_id=input("Enter Student ID")
name=input("Enter Name")
age=input("Enter Age")
city=input("Enter City")
phone=input("Enter the Phone Number")
print("\n--Student details--")
print("ID",student_id)
print("Name",name)
print("Age",age)
print("City",city)
print("Phone number",phone)


#7
a=input("Enter first number")
b=input("Enter second number")
a,b=b,a
print("After swapping")
print("First number",a)
print("Second number",b)


#8
num=int(input("Enter a number"))
result="Even" if num%2==0 else "Odd"
print("The number is ",result)
