import requests
from bs4 import BeautifulSoup

def get_yojijukugo_id(word):
    # Add your database connection and retrieval logic here
    # For example, you might use a database library like SQLAlchemy or psycopg2
    # Replace the following line with the actual logic to get the ID from the database
    return 123  # Replace with the actual ID retrieval logic

def get_jisho_sentences(word):
    url = f'https://jisho.org/search/{word}%23sentences'

    try:
        # Send an HTTP GET request to the Jisho sentences page
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <span> tags with class 'english' to get sentences
        sentence_spans = soup.find_all('span', class_='english')

        if sentence_spans:
            # Extract the text content of each <span> tag
            sentences = [span.get_text(strip=True) for span in sentence_spans]
            return sentences
        else:
            return None  # Return None if no sentences found

    except requests.exceptions.RequestException as e:
        return f"Error fetching sentences from Jisho: {e}"

# Example usage
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\onlyKanji.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\insertIntoSentenceSample.txt'

try:
    # Open the input file for reading
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Open the output file for writing
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Process each word from the file
            for line in input_file:
                word_to_search = line.strip()

                # Retrieve sentences from Jisho
                sentences = get_jisho_sentences(word_to_search)

                # Check if sentences were found
                if sentences is not None:
                    # Get the yojijukugo ID from the database
                    yojijukugo_id = get_yojijukugo_id(word_to_search)

                    # Print the word and sentences
                    print(f"Word: {word_to_search}")
                    for index, sentence in enumerate(sentences, start=1):
                        print(f"  {index}. {sentence}")

                        # Handle single quotes in the sentence
                        sentence = sentence.replace("'", "''")

                        # Write INSERT INTO statement for sentence_sample to the output file
                        insert_statement = f"INSERT INTO sentence_sample VALUES (3, (SELECT id from jojijukugo where word = '{word_to_search}'), '{sentence}');"
                        output_file.write(insert_statement + '\n')
                        output_file.flush()

                    print()

    print(f"Processing complete. Results printed to console and saved to '{output_file_path}'.")

except Exception as e:
    print(f"Error: {e}")