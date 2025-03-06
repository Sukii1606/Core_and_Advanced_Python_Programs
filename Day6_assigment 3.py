# Write a python program finding the factorial of a given number using a while loop.

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    
    fact = 1
    while n > 0:
        fact *= n
        n -= 1  # Decrement n
    return fact

num = int(input("Enter a number: "))

# Call the function and display the factorial
print(f"Factorial of {num} is:", factorial(num))

#output
#Enter a number: 5
#Factorial of 5 is: 120