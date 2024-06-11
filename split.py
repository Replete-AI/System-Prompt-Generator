import os

def split_jsonl_file(input_file, num_splits=10):
    # Step 1: Read the original JSONL file and count the lines
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    lines_per_split = total_lines // num_splits
    remainder = total_lines % num_splits

    # Step 2: Split and write the lines into smaller files
    base_name, ext = os.path.splitext(input_file)
    for i in range(num_splits):
        start_index = i * lines_per_split
        end_index = start_index + lines_per_split
        if i == num_splits - 1:
            # Add any remaining lines to the last split
            end_index += remainder
        
        split_lines = lines[start_index:end_index]
        
        output_file = f"{base_name}_part{i+1}{ext}"
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.writelines(split_lines)
        
        print(f"Written {len(split_lines)} lines to {output_file}")

# Usage example
input_file = '/home/REDACTED/Documents/Parsing/Combined/combined.jsonl'
split_jsonl_file(input_file, num_splits=10)
