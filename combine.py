import os

# Specify the directory containing the JSONL files
directory = '/home/REDACTED/Documents/Parsing/Combined/split/splitfinish'

# Specify the output file path
output_file = '/home/REDACTED/Documents/Parsing/regularization.jsonl'

# Create the output file
with open(output_file, 'w', encoding='utf-8') as outfile:
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.jsonl'):
            file_path = os.path.join(directory, filename)
            
            # Open the JSONL file and read each line
            with open(file_path, 'r', encoding='utf-8') as infile:
                for line in infile:
                    # Write each line to the output file
                    outfile.write(line)
