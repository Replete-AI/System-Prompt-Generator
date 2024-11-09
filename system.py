import json
import openai
from tqdm import tqdm

# Create client
client = openai.OpenAI(
    base_url="https://api.together.xyz/v1",
    api_key="12098ase1331d7a89a0d9wd9120391ad7awd", #definitely not my API key. nope. no way.
)

new_data = []

# Load your JSONL data
with open("/home/REDACTED/Documents/Datasets/needs_system_prompts/split/output_1.jsonl", "r") as f:
    data = [json.loads(line) for line in f]

for item in tqdm(data, desc="Processing conversations"):
    conversation = item["conversations"]
    
    # Extract the entire conversation context
    conversation_context = " ".join([msg["value"] for msg in conversation])

    # Call the LLM to generate a new system prompt
    chat_completion = client.chat.completions.create(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[
            {
                "role": "system",
                "content": "You are Pneuma, your task is to generate system prompt that used by LLM based on <chat> conversation.\nStart your response with "You are" and keep it concise. For Q&A conversation you need to choose subject or domain experts, and how the question is approached by gpt. For roleplay or writing conversation, assume gpt it was you, you need to describe gpt character based on their dialog, never ask to generate character response.",
            },
            {
                "role": "user",
                "content": f"<chat>{conversation_context}</chat>",
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
with open("/home/REDACTED/Documents/Datasets/needs_system_prompts/splitfinish/regularization_1.jsonl", "w") as f:
    for item in new_data:
        f.write(json.dumps(item) + "\n")
