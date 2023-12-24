def remove_text_from_line(input_file_path, output_file_path):
    try:
        # Open the input file for reading
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            # Read lines from the input file
            lines = input_file.readlines()

        # Process each line and remove text starting from the 5th character
        modified_lines = [line[:4] + '\n' for line in lines]

        # Open the output file for writing
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Write the modified lines to the output file
            output_file.writelines(modified_lines)

        print(f"Text removed from each line in '{input_file_path}'. Result saved to '{output_file_path}'.")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\kanjiAndKana.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\onlyKanji.txt'
remove_text_from_line(input_file_path, output_file_path)
