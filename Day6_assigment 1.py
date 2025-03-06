# Write a python program to reverse a number using a while loop. 


def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10  
        rev = (rev * 10) + digit  
        n = n // 10  
    return rev

num = int(input("Enter a number: "))

print("Reversed Number:", reverse_number(num))

#output
#Enter a number: 26548614
#Reversed Number: 41684562