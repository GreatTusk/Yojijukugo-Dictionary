import re

def insert_newline_after_hiragana(input_file, output_file):
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use a regular expression to insert newline after each hiragana followed by kanji
    result = re.sub(r'([\u3040-\u309F])([\u4E00-\u9FAF])', r'\1\n\2', content)

    # Write the result to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)

# Specify your input and output file paths
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\kanji.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\kanjiAndKana.txt'

# Call the function to insert newline after hiragana followed by kanji
insert_newline_after_hiragana(input_file_path, output_file_path)
