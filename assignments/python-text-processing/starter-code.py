# Python Text Processing Assignment
# Starter Code

# Task 1: String Manipulation
def string_manipulation():
    # Get user input
    sentence = input("Enter a sentence: ")
    
    # TODO: Reverse the sentence
    reversed_sentence = ""
    
    # TODO: Count the number of words
    word_count = 0
    
    # TODO: Convert to uppercase
    uppercase_sentence = ""
    
    # Display results
    print(f"Reversed: {reversed_sentence}")
    print(f"Word count: {word_count}")
    print(f"Uppercase: {uppercase_sentence}")

# Task 2: File I/O Operations
def file_operations():
    # TODO: Read from input.txt
    with open('input.txt', 'r') as file:
        text = file.read()
    
    # TODO: Process the text (remove punctuation, convert to lowercase)
    processed_text = ""
    
    # TODO: Write to output.txt
    with open('output.txt', 'w') as file:
        file.write(processed_text)

if __name__ == "__main__":
    string_manipulation()
    file_operations()