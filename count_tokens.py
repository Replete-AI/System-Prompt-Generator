import json
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')  # Download the 'punkt' resource

def count_tokens_in_jsonl(file_path):
    total_tokens = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            json_data = json.loads(line)
            conversations = json_data['conversations']
            for conversation in conversations:
                text = conversation['value']
                tokens = word_tokenize(text)
                total_tokens += len(tokens)
    
    return total_tokens

# Specify the path to your JSONL file
jsonl_file = '/home/REDACTED/Documents/Parsing/regularization.jsonl'

# Count the tokens
token_count = count_tokens_in_jsonl(jsonl_file)

print(f"Total tokens in the JSONL file: {token_count}")
