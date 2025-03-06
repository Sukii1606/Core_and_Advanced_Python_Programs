#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer


def get_integer():
    user_input = input("Enter an integer: ")
    
    if not user_input.lstrip('-').isdigit():
        raise ValueError("Invalid input! Please enter a valid integer.")
    
    return int(user_input)

# Using the function
try:
    number = get_integer()
    print(f"You entered: {number}")
except ValueError as e:
    print(e)

#output 1
#Enter an integer: 5
#You entered: 5
    
#Output 2
#Enter an integer: hi
#Invalid input! Please enter a valid integer.