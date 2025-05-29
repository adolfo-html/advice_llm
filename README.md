# Dad Advice LLM Project

A web application that provides general advice with the warmth, humor, and wisdom of a classic dad. Users ask questions, and the app responds with thoughtful, personalized advice - tailored by name, age, and gender - to make every answer feel like it’s coming from a real, caring father figure. Perfect for anyone wanting guidance or encouragement through any of life's hurdles.

## The Process

### Deciding on a model

I decided on using Llama3.2-3B-Instruct, a pre-trained, transformer-based large language model (LLM) for this project, because of its relatively manageable size and capablility. It's also trained to follow system prompts more accurately. I originally tried to use Llama-3.1-8B, but it required too much processing power, so Python kept terminating the process.

### Making a testing environment

Now we need to download the infrastructure necessary to actually use the model.

First, I installed the `transformers` Python library from Hugging Face in my program, which provides access to many different toolkits to run different transformer-based LLMs. It also includes tools like `AutoTokenizer` and `AutoModelForCausalLM`, which automatically load the correct tokenizer and model setup for any supported model. The library also provides a convenient pipeline function, which creates a simple interface for text generation.

Next, I installed the `torch` library in my program, which is the deep learning engine that runs the LLM. It passes the model weights through the transformer neural network to generate meaningful output.

An important step in this process was to obtain access to the Hugging Face repositories I needed. I had to make an account on huggingface.co, then create an access token. Once generated, I made it an environment variable to discreetly plug it into my Python program. The program needs this token to verify itself to the repository before importing the transformers. I imported the library `huggingface_hub` to basically authenticate the program with my token.

Then I modified the sample code provided by Hugging Face to make the pipeline, get the prompt, and .

### Making an interface

I want to make this a web application. So, now that I know that my program works, I want to establish a line of communication between a website and the Python script. For now, I'm gonna work on it locally.

So right now, my goal is to have the .html file communicate with the Python script via fetch(). This means I'll be sending an HTTP request (with the fetch function) to the Python program and waiting for a request on the front-end.

I have a lot of questions already, like if Python needs to be listening before the HTTP request is sent to it (probably), and how the AWS server is going to automatically run it. And if AWS is gonna be good enough for the program. And if I need to download the 6.4 GB vector embedding file to the server or not. But I'm getting ahead of myself.

I'll just focus on interface.html for now.