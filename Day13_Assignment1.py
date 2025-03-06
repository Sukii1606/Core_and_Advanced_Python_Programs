#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    # Taking user input for numerator and denominator
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Attempting division
    result = numerator / denominator

    # Display result
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numeric values.")

#output 1
#Enter the numerator: 5
#Enter the denominator: 8
#Result: 0.625

#Output 2
#Enter the numerator: 9
#Enter the denominator: 0
#Error: Division by zero is not allowed.