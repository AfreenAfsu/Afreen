# 1
num_products = int(input("How many products do you want to enter? "))

products = []

for i in range(num_products):
    print(f"\nEnter details for product {i+1}:")
    name = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Quantity purchased: "))
    product = (name, price, quantity)
    products.append(product)

print("\n======= BILL DETAILS =======")
print("{:<15} {:<10} {:<10} {:<10}".format("Product", "Price", "Quantity", "Total"))

total_bill = 0

for name, price, quantity in products:
    total = price * quantity
    total_bill += total
    print("{:<15} {:<10.2f} {:<10} {:<10.2f}".format(name, price, quantity, total))

print("\nTotal Bill Amount: ₹{:.2f}".format(total_bill))
