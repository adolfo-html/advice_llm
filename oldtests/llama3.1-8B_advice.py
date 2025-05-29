# This is the program I wrote when I assumed I was using Llama-3.1-8B.
# It turned out to be too RAM-intensive for my poor Optiplex 780.

# Importing Flask API for web app communication
from flask import Flask, request, jsonify


import sys
sys.path = [p for p in sys.path if not p.startswith('/usr/lib/python3/dist-packages')]
# ^ Because outdated python3 folder was being annoying


# For accessing environment variables (hidden credential variables)
import os
from dotenv import load_dotenv

load_dotenv() # Loads .env into os.environ

access_token = os.environ.get('ACCESS_TOKEN')


# Running the LLM

model_id = "meta-llama/Meta-Llama-3.1-8B"

# Manually setting the correct toolkits from transformers (requires access token)
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
tokenizer = AutoTokenizer.from_pretrained(model_id, token=access_token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=access_token)

import torch

# Create a pipeline ()

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    torch_dtype=torch.bfloat16
)

# Create a prompt
user_input = "Dad, I've been feeling sad recently. What should I do?"
prompt = "You are a wise, loving dad giving wholesome life advice. Your kid says, \"{user_input}\". What do you say?"

generated_text = generator(prompt, max_new_tokens=100, temperature=0.7, do_sample=True)

print(generated_text)

# The prompt! 

# messages = [
#     {"role": "system", "content": "You are a wise, loving dad giving wholesome life advice."},
#     {"role": "user", "content": "Dad, I've been feeling sad recently. What should I do?"},
# ]

