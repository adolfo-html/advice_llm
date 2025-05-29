import sys
sys.path = [p for p in sys.path if not p.startswith('/usr/lib/python3/dist-packages')]
# ^ Because outdated python3 folder was being annoying


# For accessing environment variables (hidden credential variables)
import os
from dotenv import load_dotenv
load_dotenv() # Loads .env into os.environ
access_token = os.environ.get('ACCESS_TOKEN')

# Authentication (required before accessing Hugging Face repos)
# Don't forget to set up server environment variables!
from huggingface_hub import login
login(token=access_token)


# Running the LLM

model_id = "meta-llama/Llama-3.2-3B-Instruct"

# Importing transformers toolkits and torch engine
import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-3B-Instruct"

# Create a pipeline (which is basically just a text generation function with parameters to define)
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# Get user input
user_input = input("Ask for advice : ")


# Create prompt
messages = [
    {"role": "system", "content": "You are a wise, loving dad giving wholesome life advice."},
    {"role": "user", "content": user_input},
]

# Generate and print output
outputs = pipe(
    messages,
    max_new_tokens=256,
)

print(outputs[0]["generated_text"][-1])

# The prompt! 

# messages = [
#     {"role": "system", "content": "You are a wise, loving dad giving wholesome life advice."},
#     {"role": "user", "content": "Dad, I've been feeling sad recently. What should I do?"},
# ]