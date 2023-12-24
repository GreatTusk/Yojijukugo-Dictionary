import requests
from bs4 import BeautifulSoup

def get_jisho_sentences(word):
    url = f'https://jisho.org/search/{word}%23sentences'

    try:
        # Send an HTTP GET request to the Jisho sentences page
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <ul> tags with class 'japanese_sentence' and lang 'ja'
        japanese_sentences = soup.find_all('ul', class_='japanese_sentence', lang='ja')

        if japanese_sentences:
            # Extract the Japanese text from each <ul> tag
            sentences = []
            for sentence_ul in japanese_sentences:
                # Extract text from <span> tags within each <li>
                japanese_text = ' '.join(li.find('span', class_='unlinked').get_text(strip=True) if li.find('span', class_='unlinked') else '' for li in sentence_ul.find_all('li'))
                sentences.append(japanese_text)

            return sentences
        else:
            return None  # Return None if no Japanese sentences found

    except requests.exceptions.RequestException as e:
        return f"Error fetching sentences from Jisho: {e}"

# Example usage
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\onlyKanji.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\insertIntoSentenceSampleJapanese2.txt'

try:
    # Open the input file for reading
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Open the output file for writing
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Process each word from the file
            for line in input_file:
                word_to_search = line.strip()

                # Retrieve Japanese sentences from Jisho
                japanese_sentences = get_jisho_sentences(word_to_search)

                # Check if Japanese sentences were found
                if japanese_sentences is not None:
    

                    # Print the word and Japanese sentences
                    print(f"Word: {word_to_search}")
                    for index, sentence in enumerate(japanese_sentences, start=1):
                        print(f"  {index}. {sentence}")

                        # Handle single quotes in the sentence
                        sentence = sentence.replace("'", "''")

                        # Write INSERT INTO statement for sentence_sample to the output file
                        insert_statement = f"INSERT INTO sentence_sample VALUES (1, (SELECT id from yojijukugo where word = '{word_to_search}'), '{sentence}');"
                        output_file.write(insert_statement + '\n')
                        output_file.flush()

                    print()

    print(f"Processing complete. Results printed to console and saved to '{output_file_path}'.")

except Exception as e:
    print(f"Error: {e}")
