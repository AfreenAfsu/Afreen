# 1
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_items = set1 | set2
print("Unique Items from both sets:", unique_items)

# 2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.symmetric_difference(set2)
print("Elements present in A or B but not both:", result )

# 3
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

common = set1.intersection(set2)

if common:
    print("Common elements:", common)
else:
    print("No common elements.")

# 4
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print("Items common to both sets:", set1)

# 5
visitor_count = int(input("How many visitors visited the website? "))

visitors = set()

for i in range(visitor_count):
    name = input(f"Enter visitor name or ID #{i+1}: ")
    visitors.add(name)

print("\nUnique Visitors List:")
print(visitors)

print("Total Number of Unique Visitors:", len(visitors))

# 6
hobbies1 = input("Enter hobbies of Friend 1 (comma separated): ")
hobbies2 = input("Enter hobbies of Friend 2 (comma separated): ")

set1 = set(hobby.strip().lower() for hobby in hobbies1.split(","))
set2 = set(hobby.strip().lower() for hobby in hobbies2.split(","))

common_hobbies = set1 & set2
all_hobbies = set1 | set2
unique_to_each = set1 ^ set2

print("\nCommon hobbies:", common_hobbies)
print("All hobbies:", all_hobbies)
print("Unique hobbies to each friend:", unique_to_each)
