# Ask user for their age
age = int(input("Enter your age: "))

# Ask user to describe their health condition
condition = input("Enter your health condition (e.g., healthy, diabetic, heart patient): ").lower()

# Check for vaccine eligibility
if age >= 60 or condition in ["diabetic", "heart patient", "asthmatic"]:
    print("Eligible for vaccine")

elif 40 <= age < 60 and condition != "healthy":
    print("Needs doctor approval")

else:
    print("Not eligible")
