import json

def transform_jsonl(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            data = json.loads(line)
            
            # Create the transformed object
            transformed_data = {
                "conversations": [
                    {"from": "system", "value": data["system"]},
                    {"from": "human", "value": data["question"]},
                    {"from": "gpt", "value": data["chosen"]}
                ]
            }
            
            # Write the transformed object to the output file
            outfile.write(json.dumps(transformed_data) + '\n')

# Usage
input_file = '/home/REDACTED/Downloads/Neural-DPO.jsonl'
output_file = 'neuraldposharegpt.jsonl'

transform_jsonl(input_file, output_file)
