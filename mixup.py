import json
from random import shuffle  # Importing shuffle from the random module

# Read the JSONL file
data = []
with open('/home/REDACTED/Documents/Parsing/finalregularization.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line))

# Shuffle the list of JSON objects
shuffle(data)  # Using the shuffle function directly

# Write the shuffled data to a new JSONL file
with open('/home/REDACTED/Documents/Parsing/regularization.jsonl', 'w') as f:
    for obj in data:
        json_str = json.dumps(obj)
        f.write(json_str + '\n')
