# This program reads a PDF file, extracts its text, and counts the frequency of each character in the text.

import pprint,PyPDF2  # Library for working with PDF files

# Specify the PDF file to process
PDF_File = 'email_phone_example.pdf'  # Replace with the path to your PDF file

try:
    # Open the PDF file in binary read mode
    with open(PDF_File, 'rb') as pdfFile:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(pdfFile)
        
        # Get the total number of pages in the PDF
        length_of_file = len(reader.pages)
        print(f'File pages : {length_of_file}')  # Display the number of pages

        # Initialize a list to store text from all pages
        all_pages = []
        
        # Loop through each page in the PDF
        for page in range(length_of_file):
            # Extract text from the current page
            extract = reader.pages[page].extract_text()
            # Append the extracted text to the list
            all_pages.append(extract)

    # Combine all extracted text into a single string
    all_text = '\n'.join(all_pages)

    # Initialize a dictionary to store character frequencies
    count = {}
    # Variable to count the total number of characters
    all_characters = 0
    
    # Loop through each character in the combined text
    for char in all_text:
        # Add the character to the dictionary if not already present, with an initial count of 0
        count.setdefault(char, 0)
        # Increment the count for the character
        count[char] += 1
        # Increment the total character count
        all_characters += 1

    # Write the character frequencies and total count to a file
    with open('count_character.txt', 'w', encoding='utf-8') as write_count:
        # Write the dictionary of character frequencies in a readable format
        write_count.write(pprint.pformat(count))
        # Write the total number of characters
        write_count.write(f'\nTotal different characters: {all_characters}')

    # Display the character frequencies in the console
    pprint.pprint(count)
    # Display the total number of characters
    print(f'Total different characters: {all_characters}')

# Handle the case where the specified PDF file is not found
except FileNotFoundError:
    print(f"Error: The file '{PDF_File}' was not found.")
# Handle any other exceptions that may occur
except Exception as e:
    print(f"An error occurred: {e}")
