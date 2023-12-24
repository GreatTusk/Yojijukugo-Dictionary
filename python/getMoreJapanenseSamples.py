import requests
from bs4 import BeautifulSoup

def get_sentences(word):
    url = f"https://dictionary.goo.ne.jp/word/{word}/"

    try:
        # Use a different method to make the request
        with requests.get(url) as response:
            response.raise_for_status()

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <dt> elements
            dt_elements = soup.find_all('dt')

            # Iterate through <dt> elements to find "用例"
            for dt_element in dt_elements:
                if "用例" in dt_element.get_text():
                    # Find the corresponding <dd> element
                    dd_element = dt_element.find_next('dd')

                    if dd_element:
                        example_text = dd_element.text.strip()
                        return [example_text]  # Return the example text as a list

            return None  # Return None if example not found

    except requests.exceptions.RequestException as e:
        return [f"Error fetching the URL: {e}"]
    except Exception as e:
        return [f"Error: {e}"]





# Example usage
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\onlyKanji.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\insertIntoSentenceSampleJapanese.txt'

try:
    # Open the input file for reading
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        # Open the output file for writing
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            # Process each word from the file
            for line in input_file:
                word_to_search = line.strip()
                print(line)
                # Retrieve sentences from the provided method
                sentences = get_sentences(word_to_search)

                # Check if sentences were found
                if sentences is not None:
                    # Print the word and sentences
                    print(f"Word: {word_to_search}")
                    for index, sentence in enumerate(sentences, start=1):
                        print(f"  {index}. {sentence}")

                        # Handle single quotes in the sentence
                        sentence = sentence.replace("'", "''")

                        # Write the original INSERT INTO statement for sentence_sample to the output file
                        insert_statement = f"INSERT INTO sentence_sample VALUES (1, (SELECT id from yojijukugo where word = '{word_to_search}'), '{sentence}');"
                        output_file.write(insert_statement + '\n')
                        output_file.flush()

                    print()
                else:
                    print("Sentence is none")
    print(f"Processing complete. Results printed to console and saved to '{output_file_path}'.")

except Exception as e:
    print(f"Error: {e}")
