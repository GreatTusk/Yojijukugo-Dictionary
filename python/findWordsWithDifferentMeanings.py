from collections import Counter

def find_repeated_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    words = [line.strip() for line in lines]

    word_counts = Counter(words)
    repeated_words = [word for word, count in word_counts.items() if count > 1]

    return repeated_words

if __name__ == "__main__":
    filename = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\onlyKanji.txt'  # Replace with the actual filename

    repeated_words = find_repeated_words(filename)

    if repeated_words:
        print("Repeated words:")
        for word in repeated_words:
            print(word)
    else:
        print("No repeated words found.")
