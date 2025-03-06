#Write a Python program to remove duplicate characters of a given string. 
#Input = “String and String Function” 
#Output: String and Function

def remove_duplicate_chars(s):
    result = ""
    seen = set()
    
    for ch in s:
        if ch not in seen or ch == " ":
            result += ch
            seen.add(ch)
    
    return result

# Given input string
input_string = "String and String Function"
output_string = remove_duplicate_chars(input_string)
print("Output:", output_string)

#output
#Output: String ad  Fuco