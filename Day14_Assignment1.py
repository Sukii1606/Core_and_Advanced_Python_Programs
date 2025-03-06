#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen

def read_file_line_by_line(filename="ABC.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())  # Remove trailing newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Call the function
read_file_line_by_line()

#output
#The sun sets behind the hills, painting the sky in shades of orange and pink.
#A cat lazily stretches on the windowsill, watching the world go by.
#Raindrops tap against the glass, a rhythmic melody of nature.
#Lost in thought, she scribbled poetry in the margins of her notebook.
#The aroma of fresh coffee filled the air, a warm embrace on a cold morning.
#He glanced at the old photo, memories flooding back in waves.
#The city lights flickered like stars fallen from the sky.
#An unread book sat on the shelf, waiting to tell its story.
#Waves crashed against the shore, whispering secrets of the deep.
#Time moves forward, but some moments remain frozen forever.