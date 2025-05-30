# Dad Advice LLM Project

A web application that provides general advice with the warmth, humor, and wisdom of a classic dad. Users ask questions, and the app responds with thoughtful, personalized advice - tailored by name, age, and gender - to make every answer feel like it’s coming from a real, caring father figure. Perfect for anyone wanting guidance or encouragement through any of life's hurdles.

## The Process

Here's how I made my decisions and built a working web app throughout the project! 

### Deciding on a model

I decided on using **Llama3.2-3B-Instruct**, a pre-trained, transformer-based *large language model* (LLM) for this project, because of its relatively manageable size and capablility. It's also trained to follow system prompts more accurately. I originally tried to use Llama-3.1-8B, but it loaded too much data into my cache, so Python kept terminating the process.

My Python program uses the **Hugging Face** repository for the Llama model. It authenticates itself with my access token, then loads the model into its parent device's memory for the generation part.


### Making a testing environment

Now we need to download the infrastructure necessary to actually use the model.

First, I installed the `transformers` Python library from Hugging Face in my program, which provides access to many different toolkits to run different transformer-based LLMs. It also includes tools like `AutoTokenizer` and `AutoModelForCausalLM`, which automatically load the correct tokenizer and model setup for any supported model. The library also provides a convenient pipeline function, which creates a simple interface for text generation.

Next, I installed the `torch` library in my program, which is the deep learning engine that runs the LLM. It passes the model weights through the transformer neural network to generate meaningful output.

An important step in this process was to obtain access to the Hugging Face repositories I needed. I had to make an account on huggingface.co, then create an access token. Once generated, I made it an environment variable to discreetly plug it into my Python program. The program needs this token to verify itself to the repository before importing the transformers. I imported the library `huggingface_hub` to basically authenticate the program with my token.

Then I modified the sample code provided by Hugging Face to make the pipeline, get the prompt, and run the model.

### Making an interface

I want to make this a web application. So, now that I know that my program works, I want to establish a line of communication between a website and the Python script. For now, I'm gonna work on it locally.

So right now, my goal is to have the .html file communicate with the Python script via fetch(). This means I'll be sending an HTTP request (with the fetch function) to the Python program and waiting for a request on the front-end.

I have a lot of questions already, like if Python needs to be listening before the HTTP request is sent to it (probably), and how the AWS server is going to automatically run it. And if AWS is gonna be good enough for the program. And if I need to download the 6.4 GB vector embedding file to the server or not. But I'm getting ahead of myself.

I decided on using **Flask API** to construct a web interface between the Python program and a website. Flask is a Python library that provides easy setup for RESTful APIs that other software applications can use. Flask runs a server and listens for HTTP requests, just like Node.js would!!

It was at this point that I realized I actually wasn't using the 6.4 GB Llama model I downloaded directly from Llama! While testing, I noticed my Python program authenticates into the Hugging Face repository, then loads the model into my computer's cache. It doesn't call the data from the vector embedding file I have on my computer. It won't even know how to use it in its current state - The model I downloaded straight from Llama requires tools that work differently from the ones in the Hugging Face transformers library, so they're incompatible. So I have this whole AI on my computer for no reason. Cool. But, this is actually great, for two reasons. One, the server won't need to have the huge file uploaded to it - it can load the model into its cache *on disk*, so the server only has to download it once (I don't have to upload it to a database like I thought). So even if the server restarts, as long as the storage persists, it won't need to download the model again. Two, minimal setup. I don't have to change much about the JavaScript code other than where it's sending the fetch request. At least, I hope not. We'll see!

### Hosting a server

Amazon Web Services (AWS) has a lot of services. Time to see if they're free or not. (They're not.)

Commonly visited AWS services include EC2, S3, Aurora and RDS, and Lambda. S3, Aurora and RDS are database things, while EC2 and Lambda are server platforms.

**EC2** (Elastic Compute Cloud) is AWS's virtual server service. Benefits of this service include customizable hardware and software configurations, complete control over customization, and on-demand availability.

***But the free plan has like 1 GB of RAM!!!*** Are you kidding me!!?

Here, I've hit a roadblock - I don't have enough virtual resources to have my program generate responses in only seconds. Really kills the convenience aspect.