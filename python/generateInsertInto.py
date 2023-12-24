def generate_insert_statements_and_write(input_file, output_file, table_name, sequence_name):
    statements = []

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                # Extract the first four characters as the 'word' and the rest as 'reading'
                word = line[:4]
                reading = line[4:]

                # Generate the INSERT INTO statement for yojijukugo
                yojijukugo_insert_statement = f"INSERT INTO {table_name} (id, word) VALUES ({sequence_name}.NEXTVAL, '{word}');"
                statements.append(yojijukugo_insert_statement)

                # Extract the generated id for yojijukugo using the sequence
                id_yojijukugo = f"{sequence_name}.CURRVAL"

                # Generate the INSERT INTO statement for reading
                reading_insert_statement = f"INSERT INTO reading (id_yojijukugo, reading) VALUES ((SELECT id FROM yojijukugo where word = '{word}'), '{reading}');"
                statements.append(reading_insert_statement)

    # Write the generated statements to the output file
    with open(output_file, 'w', encoding='utf-8') as output_file:
        for statement in statements:
            output_file.write(statement + '\n')

# Specify your input and output file paths, table name, and sequence name
input_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\kanjiAndKana.txt'
output_file_path = r'C:\Users\f_776\Documents\NetBeansProjects\Yojijukugo Dictionary\txt\insertYojijukugo.txt'
table_name = 'yojijukugo'
sequence_name = 'seq_yojijukugo'

# Generate INSERT INTO statements and write to the output file
generate_insert_statements_and_write(input_file_path, output_file_path, table_name, sequence_name)

print(f"Generated INSERT INTO statements written to {output_file_path}")
