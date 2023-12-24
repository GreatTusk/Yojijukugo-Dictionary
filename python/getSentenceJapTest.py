import requests
from bs4 import BeautifulSoup
import re
import html

def fix_sentence_format(sentence):
    # Remove spaces around single quotes
    fixed_sentence = re.sub(r'\s*\'\s*', "'", sentence)
    
    # Remove spaces before periods, except when followed by an uppercase letter or there is no text after the period
    fixed_sentence = re.sub(r'\s*\.(?=[^a-z]|$)', '.', fixed_sentence)

    return fixed_sentence



def get_sentences(word):
    url = f"https://tangorin.com/sentences?search={word}"

    # Make a request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all entry elements
        entries = soup.find_all('div', class_='entry')

        eng_list = []
        jap_list = []

        for entry in entries:
            # Extract the text within the specified HTML elements for each entry
            dt_element = entry.find('dt', class_='s-jp')
            dd_element = entry.find('dd', class_='s-en')

            if dt_element and dd_element:
                dt_text = dt_element.get_text(strip=True)

                # Extract text within <span> tags for English text
                dd_text_span = dd_element.find('span')
                dd_text = dd_text_span.get_text(separator=' ') if dd_text_span else ""

                # Use html.unescape to convert HTML entities to regular characters
                dd_text = html.unescape(dd_text)

                # Replace spaces around single quotes
                dd_text = re.sub(r"\s'(\S)", r"'\1", re.sub(r"(\S)'\s", r"\1'", dd_text))

                # Replace spaces around the period
                dd_text = re.sub(r"\.\s", ". ", dd_text)

                # Replace consecutive spaces with a single space
                dd_text = re.sub(r'\s+', ' ', dd_text).strip()

                eng = fix_sentence_format(dd_text)
                

                print("Japanese Text:")
                print(dt_text)
                jap_list.append(dt_text)

                print("\nEnglish Text:")
                print(eng)
                eng_list.append(eng)

                print("\n---\n")  # Add a separator between entries
        return eng_list, jap_list
    else:
        print(f"Error: Unable to fetch content. Status code: {response.status_code}")
        return None


def main():
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
                    # Retrieve sentences from the provided method
                    eng_list, jap_list = get_sentences(word_to_search)

                    # Check if sentences were found
                    if eng_list and jap_list:
                        # Print the word and sentences
                        print(f"Word: {word_to_search}")
                        for index, (eng_sentence, jap_sentence) in enumerate(zip(eng_list, jap_list), start=1):
                            print(f"  {index}. English: {eng_sentence}")
                            print(f"     Japanese: {jap_sentence}")

                            # Handle single quotes in the English sentence
                            eng_sentence = eng_sentence.replace("'", "''")

                            # Write the original INSERT INTO statement for sentence_sample to the output file
                            insert_statement = f"INSERT INTO sentence_sample VALUES (1, (SELECT id from yojijukugo where word = '{word_to_search}'), '{jap_sentence}');"
                            insert_statement2 = f"INSERT INTO sentence_sample VALUES (3, (SELECT id from yojijukugo where word = '{word_to_search}'), '{eng_sentence}');"
                            output_file.write(insert_statement + '\n')
                            output_file.write(insert_statement2 + '\n')
                            output_file.flush()

                        print()
                    else:
                        print(f"No sentences found for '{word_to_search}'")

        print(f"Processing complete. Results printed to console and saved to '{output_file_path}'.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()