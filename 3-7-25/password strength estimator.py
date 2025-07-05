# Ask user to enter a password
password = input("Enter your password: ")

# Check if it's too short
if len(password) < 8:
    print("Too Short")

else:
    has_digit = False
    has_letter = False

    # Loop through each character in the password
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_letter = True
        
        # If both are found, no need to keep checking
        if has_digit and has_letter:
            break

    # Final strength check
    if has_digit and has_letter:
        print("Strong")
    else:
        print("Weak")
