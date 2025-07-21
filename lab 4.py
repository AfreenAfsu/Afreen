# 1
students = ["Alice", "Bob", "Charlie"]

# Add a student
students.append("David")

# Remove a student
students.remove("Bob")

print("Student List:", students)

# 2
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even Numbers from 1 to 20:", even_numbers)

# 3
marks = [85, 90, 78, 92, 88]
average = sum(marks) / len(marks)
print("Average Marks:", average)

# 4
shopping_cart = ["apple", "banana", "milk", "bread"]
product = "milk"

if product in shopping_cart:
    print(f"{product} is available in the shopping cart.")
else:
    print(f"{product} is not available.")

# 5
names = ["John", "Alice", "John", "David", "Alice", "John"]
count = names.count("John")
print("John appears", count, "times in the list.")
