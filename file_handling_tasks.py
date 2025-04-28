# 1. Create File: Write "Hello, world!" to a text file
def create_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, world!\n")

# 2. Read File: Read and print contents of a file
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    print(content)

# 3. Append File: Add a new line to an existing file
def append_file(filename, new_line):
    with open(filename, 'a') as file:
        file.write(new_line + '\n')

# 4. Count Lines: Count total number of lines in a text file
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)

# 5. Find Word: Count how many times a word appears in a file
def find_word(filename, word):
    with open(filename, 'r') as file:
        content = file.read()
    words = content.lower().split()
    return words.count(word.lower())

# 6. Copy File: Copy contents from one file to another
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)

# 7. Replace Word: Replace a word in the file with another
def replace_word(filename, old_word, new_word):
    with open(filename, 'r') as file:
        content = file.read()
    new_content = content.replace(old_word, new_word)
    with open(filename, 'w') as file:
        file.write(new_content)
