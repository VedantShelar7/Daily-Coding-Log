# Take input from user
n = int(input("Enter the number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop to print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end=" ")                        #prevents Python from going to a new line after each number.
    # Move to next line after inner loop
    print()
