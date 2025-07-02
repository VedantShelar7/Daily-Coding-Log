def unit_converter():
    print("Choose a conversion:")
    print("1. Meters to Feet")
    print("2. Kilograms to Pounds")
    print("3. INR to USD")
    
    choice = input("Enter 1/2/3: ")
    value = float(input("Enter the value to convert: "))

    if choice == "1":
        print(f"{value} meters = {value * 3.28084:.2f} feet")
    elif choice == "2":
        print(f"{value} kg = {value * 2.20462:.2f} pounds")
    elif choice == "3":
        print(f"{value} INR = {value * 0.012:.2f} USD (approx)")
    else:
        print("Invalid choice.")