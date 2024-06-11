import json
import openai

# Create client
client = openai.OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key="awd12387awadwd12i120398ada", # definitely not my API key, I have no clue why you think I'd accidentally put this in here
)

new_data = []

# Load your JSONL data
with open("/home/REDACTED/Documents/Parsing/Combined/split/combined_part10.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

for item in data:
    conversation = item["conversations"]
    
    # Extract the entire conversation context
    conversation_context = " ".join([msg["value"] for msg in conversation])

    # Call the LLM to generate a new system prompt
    chat_completion = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[
            {
                "role": "system",
                "content": "Concisely describe the function and purpose of the conversation, in the past tense. Describe it as if you were the field: \"gpt\" during the conversation. The GPT's name is Pneuma, never refer to yourself as \"The GPT\". Do not say or do anything else, just provide the description. (never use the term \"AI assistant\")",
            },
            {
                "role": "user",
                "content": f"Context: {conversation_context}",
            },
        ],
    )

    generated_system_prompt = chat_completion.choices[0].message.content

    # Find and replace the original system prompt with the generated one
    system_message = next((msg for msg in conversation if msg["from"] == "system"), None)
    if system_message:
        system_message["value"] = generated_system_prompt

    new_data.append(item)

# Save the new dataset to a JSONL file
with open("/home/REDACTED/Documents/Parsing/Combined/split/splitfinish/finish_part10.jsonl", "w") as f:
    for item in new_data:
        f.write(json.dumps(item) + "\n")
