import sys
sys.path = [p for p in sys.path if not p.startswith('/usr/lib/python3/dist-packages')]
# ^ Because outdated python3 folder was being annoying


import os
from dotenv import load_dotenv
load_dotenv() # Loads .env into os.environ
access_token = os.environ.get('ACCESS_TOKEN')


# Authentication (required before accessing Hugging Face repos)
# Don't forget to set up server environment variables!
from huggingface_hub import login
login(token=access_token)

# Importing transformers toolkits and torch engine
import torch
from transformers import pipeline


# Flask API - respond to HTTP requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Disable CORS security (annoying)

@app.route('/generate', methods=['POST']) # Specify the URL route it's listening on, and the type of HTTP requests it'll respond to


# Function to run on received HTTP request

def processInput():
    # Get user input from received HTTP request, unJSONify
    userInput = request.get_json().get("input")

    # Running the LLM starts here!

    model_id = "meta-llama/Llama-3.2-3B-Instruct"

    # Create a pipeline (which is basically just a text generation function with parameters to define)
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

    # Create prompt
    prompt = [
        {"role": "system", "content": "You are a wise, loving dad giving wholesome life advice."},
        {"role": "user", "content": userInput},
    ]

    # Generate output
    outputText = pipe(
        prompt,
        max_new_tokens=256,
    )

    reply = outputText[0]['generated_text'][-1]['content'] # isolate response

    # End LLM Run
    print(reply) # Print response in server console

    # Format response in JSON, then send
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run() # Specify the port you want to run this program on with app.run(port=number between 1025-49151)!
# Flask runs on port 5000 by default.