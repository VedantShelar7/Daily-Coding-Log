items = []
prices = []

n = int(input("How many items? "))

for i in range(n):
    item = input(f"Enter item {i+1} name: ")
    price = float(input(f"Enter price of {item}: "))
    items.append(item)
    prices.append(price)

total = sum(prices)

print("\n--- Your Receipt ---")
for i in range(n):
    print(f"{items[i].ljust(15)} ₹{prices[i]:.2f}")
print("-" * 22)
print(f"{'Total'.ljust(15)} ₹{total:.2f}")



