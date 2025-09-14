# PDF Character Frequency Analyzer

This Python program reads a PDF file, extracts its text, and calculates the frequency of each character in the text. The results are displayed in the console and saved to a text file for further analysis.

---

## Features
- Extracts text from all pages of a PDF file.
- Counts the frequency of each character in the extracted text.
- Saves the character frequency data to a text file (`count_character.txt`).
- Displays the total number of unique characters in the PDF.

---

## Requirements
- Python 3.6 or higher
- Libraries:
  - `PyPDF2` (for reading PDF files)
  - `pprint` (for pretty-printing the results)

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Nadim-Alamleh/PDF-Character-Frequency-Analyzer.git
   ```

2.Navigate to the project directory:
cd PDF-Character-Frequency-Analyzer

3.Install the required libraries:
pip install PyPDF2

Usage
1.Place the PDF file you want to analyze in the same directory as the script.
2.Update the PDF_File variable in the script with the name of your PDF file:
PDF_File = 'your_pdf_file.pdf'

3.Run the script:
python Count_program.py

4.The program will:
    Display the total number of pages in the PDF.
    Count the frequency of each character in the text.
    Save the results to count_character.txt.

Output

Console Output:
    The frequency of each character is displayed in the console.
    The total number of unique characters is printed.

Text File Output:
    A file named count_character.txt is created, containing:
    The frequency of each character in a readable format.
The total number of unique characters.
Example
Input:
A PDF file named email_phone_example.pdf with the following content:


Page 1: Hello World!Page 2: Python is awesome.
Output:
Console:


File pages : 2{' ': 4, '!': 1, '.': 1, 'H': 1, 'P': 1, 'W': 1, 'a': 1, 'd': 1, 'e': 3, 'h': 1, 'i': 1, 'l': 3, 'm': 1, 'n': 1, 'o': 3, 'r': 1, 's': 1, 't': 1, 'y': 1}Total different characters: 24
Text File (count_character.txt):


{' ': 4, '!': 1, '.': 1, 'H': 1, 'P': 1, 'W': 1, 'a': 1, 'd': 1, 'e': 3, 'h': 1, 'i': 1, 'l': 3, 'm': 1, 'n': 1, 'o': 3, 'r': 1, 's': 1, 't': 1, 'y': 1}Total different characters: 24
Error Handling
If the specified PDF file is not found, the program will display an error message:

Error: The file 'your_pdf_file.pdf' was not found.
If any other error occurs, it will be displayed in the console.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

Author
Nadim Alamleh

For any questions or feedback, feel free to reach out! ```