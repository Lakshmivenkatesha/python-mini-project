def fahrenheit_to_celsius(fahrenheit):
    # Formula: (F - 32) * 5/9 = C
    return (fahrenheit - 32) * 5 / 9

try:
        # Get input from the user
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        
        # Convert to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)
        
        # Display the result
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
except ValueError:
        print("Invalid input! Please enter a valid number.")