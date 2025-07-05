# Set the correct password
correct_password = "letmein"

# Set number of attempts
attempts = 3

# Loop until attempts run out
while attempts > 0:
    entered = input("Enter password: ")

    if entered == correct_password:
        print("Welcome!")
        break
    else:
        attempts -= 1
        print(f"Incorrect. {attempts} attempt(s) left.")

# This else runs only if while loop ends naturally (no break)
else:
    print("Locked Out")


   
