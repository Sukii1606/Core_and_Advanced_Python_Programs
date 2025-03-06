# Write a python program to check whether a number is palindrome or not? 


def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10  
        rev = (rev * 10) + digit  r
        n = n // 10  
    return original == rev  

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a Palindrome.")
else:
    print(f"{num} is not a Palindrome.")

#output
#Enter a number: 5648
#5648 is not a Palindrome.

#output 2
#Enter a number: 1221
#1221 is a Palindrome.