# Simple Interest formula: SI = (P * R * T) / 100

# Input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (in %): "))
time = float(input("Enter the time duration (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Output the result
print(f"The Simple Interest is: {simple_interest}")