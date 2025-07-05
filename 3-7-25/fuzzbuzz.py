#Loop through numbers from 1 to 50
for num in range(1, 51):
    # Check if divisible by both 3 and 5 first
    if num % 3 == 0 and num % 5 == 0:
        print("SwiftBolt")
    elif num % 3 == 0:
        print("Swift")
    elif num % 5 == 0:
        print("Bolt")
    else:
        print(num)



