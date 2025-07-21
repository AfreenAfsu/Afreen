# 1
text = input("Enter a string:")
text=text.lower()
if text==text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# 2
text=input("Enter a string")
text=text.lower()
vowels='jeaol'
count=0
for char in text:
    if char in vowels:
        count+=1
print("Number of vowels:",count)

# 3
text=input("Enter a string:")
modified_text=text.replace(" ","_")
print("Modified string:",modified_text)

# 4
password=input("Enter your password:")
has_upper=any(char.isupper() for char in password)
has_digit=any(char.isdigit() for char in password)
is_long_enough=len(password)>=8
if has_upper and has_digit and is_long_enough:
    print("Password is valid")
else:
    print("Password is invalid")

# 5
email=input("Enter your email:")
domain=email.split('@')[1]
print("Domain:",domain)
