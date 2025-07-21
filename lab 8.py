# 1
marks = []

for i in range(5):
    try:
        mark = int(input(f"Enter marks for subject {i+1}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Invalid mark! Marks should be between 0 and 100.")
        marks.append(mark)
    except ValueError as e:
        print("Error:", e)
        break

# 2
try:
    email = input("Enter your email: ")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    print("Email is valid.")
except ValueError as e:
    print("Error:", e)

# 3
correct_username = "admin"
correct_password = "1234"

for attempt in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")

else:
    raise PermissionError("Login failed 3 times. Access denied.")

# 4
try:
    password = input("Enter your password: ")
    if len(password) < 8:
        raise ValueError("Weak password")
    print("Password accepted.")
except ValueError as e:
    print("Error:", e)
    
# 5
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError("Negative number is not allowed")
    else:
        print("You entered:", num)
except NegativeNumberError as e:
    print("Error:", e)
except ValueError:
    print("Invalid input. Please enter an integer.")


