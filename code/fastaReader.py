file_path_in = "../data/nonexistent.fasta"

# Initiate variables
fasta_dict = {}
current_sequence_id = None
current_sequence = []

with open(file_path_in, 'r') as fasta_file:
    for line in fasta_file:
        line = line.strip()
        if line.startswith('>'):
            # If a new sequence header is encountered, store the previous sequence (if any)
            if current_sequence_id is not None:
                fasta_dict[current_sequence_id] = ''.join(current_sequence)
            # Extract the sequence ID from the header (remove the '>') and reset the current_sequence
            current_sequence_id = line[1:]
            current_sequence = []
        else:
            # Append the sequence line to the current sequence
            current_sequence.append(line)

    # Add the last sequence to the dictionary
    if current_sequence_id is not None:
        fasta_dict[current_sequence_id] = ''.join(current_sequence)


def split(input_string, max_length):
    # Initialize an empty list to store the divided strings
    result = []

    # Loop through the input string with a step size of max_length
    for i in range(0, len(input_string), max_length):
        # Slice the string to get a portion of max_length characters
        substring = input_string[i:i + max_length] + "\n"
        # Append the substring to the result list
        result.append(substring)

    return result


with open(file_path_out, 'w') as mod_fasta:

    for key, value in fasta_dict.items():
        mod_fasta.write(key + '\n')
        #Done