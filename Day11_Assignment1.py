#Write a Python program to Count all letters, digits, and special symbols from the given 
#string Input = “P@#yn26at^&i5ve”
#Output: Chars = 8 Digits = 2 Symbol = 3 

def count_elements(s):
    chars, digits, symbols = 0, 0, 0
    
    for ch in s:
        if ch.isalpha():
            chars += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1
    
    print(f"Chars = {chars}")
    print(f"Digits = {digits}")
    print(f"Symbol = {symbols}")

# Given input string
input_string = "P@#yn26at^&i5ve"
count_elements(input_string)

#output
#Chars = 8
#Digits = 3
#Symbol = 4