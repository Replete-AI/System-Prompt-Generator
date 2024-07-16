import json
import openai
import time
from tqdm import tqdm

# Create client
client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="gsk_Not_My_API",
)

# Load your JSONL data
with open("/home/kquant/Documents/Code/dataset-stuff/system_prompt_gen_split/system_prompt_generator/generated_conversations.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

# Open the output file for writing
with open("/home/kquant/Documents/Code/dataset-stuff/system_prompt_gen_split/system_prompt_generator/nemotron-final.jsonl", "w") as f:
    for item in tqdm(data, desc="Processing conversations"):
        conversation = item["conversations"]
        
        # Extract the entire conversation context
        conversation_context = " ".join([msg["value"] for msg in conversation])

        # Create the user prompt with the system prompt and conversation context
        user_prompt = f"Concisely describe the function and purpose of the conversation, in the past tense. Describe it as if you were the field: \"gpt\" during the conversation. The GPT's name is Pneuma, never refer to yourself as \"The GPT\". Do not say or do anything else, just provide the description. (never use the term \"AI assistant\")\n\nContext: {conversation_context}"

        # Retry the API call up to 3 times
        retry_count = 0
        while retry_count < 3:
            try:
                # Call the LLM to generate a new system prompt
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    model="llama3-8b-8192",
                )
                break  # Break the loop if the API call succeeds
            except openai.InternalServerError as e:
                print(f"Error occurred: {e}")
                retry_count += 1
                if retry_count < 3:
                    print(f"Retrying in 70 seconds... (Attempt {retry_count})")
                    time.sleep(70)  # Pause for 70 seconds before retrying
                else:
                    print("Max retries reached. Skipping this conversation.")
                    continue  # Skip to the next conversation if max retries reached

        if retry_count == 3:
            continue  # Skip to the next conversation if max retries reached

        generated_system_prompt = chat_completion.choices[0].message.content

        # Add the generated system prompt to the beginning of the conversation
        conversation.insert(0, {"from": "system", "value": generated_system_prompt})

        # Write the modified item to the JSONL file immediately
        f.write(json.dumps(item) + "\n")
        f.flush()  # Ensure the data is written to disk

        # Rate limiting: Pause for 1 second after each request to stay within the 6k tokens per minute limit
        time.sleep(1)
