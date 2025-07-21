# 1
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

total = sum(test_dict.values())
count = len(test_dict)
mean = total / count

print("Mean:", mean)

# 2
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Concatenated Dictionary:", result)

# 3
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Keys:")
for key in dict_num.keys():
    print(key)

print("\nValues:")
for value in dict_num.values():
    print(value)

print("\nItems:")
for item in dict_num.items():
    print(item)

# 4
input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

print("Keys:")
for key in input_dict.keys():
    print(key)

print("\nValues:")
for value in input_dict.values():
    print(value)

print("\nItems:")
for key, value in input_dict.items():
    print((key, value))

# 5
employees = {
    101: {"name": "Suhan", "department": "HR", "salary": 50000},
    102: {"name": "Shree", "department": "Manager", "salary": 45000},
    103: {"name": "Arbaz", "department": "finance", "salary": 38000}
}

emp_id = int(input("Enter Employee ID: "))

if emp_id in employees:
    emp = employees[emp_id]
    print("Name:", emp["name"])
    print("Department:", emp["department"])
    print("Salary:", emp["salary"])
else:
    print("Employee not found!")

