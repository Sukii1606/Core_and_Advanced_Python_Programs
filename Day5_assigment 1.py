# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 


def div(a, b):
    if b == 0:
        return "Division by zero is not allowed"
    return a / b

result = div(10, 2)
print("Division:", result)

#output
#Division: 5.0
