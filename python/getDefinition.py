import requests
from bs4 import BeautifulSoup

def get_jisho_definition(word):
    url = f'https://jisho.org/search/{word}'
    
    try:
        # Send an HTTP GET request to the Jisho page
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the <span> tag with class 'meaning-meaning' to get the definition
        definition_span = soup.find('span', class_='meaning-meaning')

        if definition_span:
            # Extract the text content of the <span> tag
            definition = definition_span.get_text(strip=True)
            return definition
        else:
            return f"No definition found for '{word}' on Jisho."

    except requests.exceptions.RequestException as e:
        return f"Error fetching data from Jisho: {e}"

# Example usage
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\onlyKanji.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\insertIntoDefinition.txt'

try:
    # Open the input file for reading
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Open the output file for writing
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Process each word from the file
            counter = 0
            for line in input_file:
                word_to_search = line.strip()

                # Retrieve the definition from Jisho
                definition = get_jisho_definition(word_to_search)

                # Print the word, definition, and the INSERT INTO statement
                #print(f"Word: {word_to_search}")
                #print(f"Definition: {definition}")

                # Handle single quotes in the definition
                definition = definition.replace("'", "''")

                # Split multiple definitions into separate statements
                definitions = [d.strip() for d in definition.split(';')]

                for single_definition in definitions:
                    insert_statement = f"INSERT INTO definition VALUES (3, (SELECT ID FROM yojijukugo WHERE word = '{word_to_search}'), '{single_definition}');"
                    #print(insert_statement)

                    # Write the INSERT INTO statement to the output file
                    output_file.write(insert_statement + '\n')
                    output_file.flush()

                print()

    print(f"Processing complete. Results printed to console and saved to '{output_file_path}'.")

except Exception as e:
    print(f"Error: {e}")
