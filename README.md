# Dad Advice LLM Project

A web application that provides general advice with the warmth, humor, and wisdom of a classic dad. Users ask questions, and the app responds with thoughtful, personalized advice - tailored by name, age, and gender - to make every answer feel like it’s coming from a real, caring father figure. Perfect for anyone wanting guidance or encouragement through any of life's hurdles.

## The Process

### Deciding on a model

I decided on using Llama3.1-8B, a pre-trained, transformer-based large language model (LLM) for this project, because of its relatively manageable size and capablility.

### Making a testing environment

Now we need to download the infrastructure necessary to actually use the model.

First, I installed the `transformers` Python library from Hugging Face in my program, which provides access to many different toolkits to run different transformer-based LLMs. It also includes tools like `AutoTokenizer` and `AutoModelForCausalLM`, which automatically load the correct tokenizer and model setup for any supported model. The library also provides a convenient pipeline function, which creates a simple interface for text generation.

Next, I installed the `torch` library in my program, which is the deep learning engine that runs the LLM. It passes the model weights through the transformer neural network to generate meaningful output.