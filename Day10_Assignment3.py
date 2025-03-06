# Write a Python program to find duplicate values from a list and display those.

def find_duplicates(lst):
    duplicates = []
    seen = {}

    for num in lst:
        if num in seen:
            if seen[num] == 1:  # Add to duplicates only once
                duplicates.append(num)
            seen[num] += 1
        else:
            seen[num] = 1

    return duplicates

# Example usage
numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 1]
print("Duplicate values:", find_duplicates(numbers))

#Output
#Duplicate values: [2, 3, 1]