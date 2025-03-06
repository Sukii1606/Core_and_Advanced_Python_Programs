#Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file(filename="ABC.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            word_count = len(content.split())  # Splitting by whitespace to count words
            print(f"Total number of words in '{filename}': {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Call the function
count_words_in_file()

#output
#Total number of words in 'ABC.txt': 116