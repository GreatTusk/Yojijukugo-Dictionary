import re

def keep_non_western_characters(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use a regular expression to match Western characters (assuming the file contains only text)
    western_pattern = re.compile('[\u0000-\u007F]+')
    result = western_pattern.sub('', content)

    # Write the result to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)

# Specify your input and output file paths
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\PAGE.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\kanji.txt'

# Call the function to keep non-Western characters
keep_non_western_characters(input_file_path, output_file_path)
