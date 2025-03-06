# Write a Python program to get the largest and smallest number from a list without built in functions. 

def find_min_max(lst):
    if not lst:
        return None, None  # Handle empty list case

    smallest = largest = lst[0]

    for num in lst[1:]:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

# Example usage
numbers = [3, 1, 7, 5, 9, 2]
smallest, largest = find_min_max(numbers)
print("Smallest number:", smallest)
print("Largest number:", largest)

#output
#Smallest number: 1
#Largest number: 9
