# LocalAI
A repo for experiments in building, fine-tuning, and running open-source/open-weight AI models in a local, private, and sometimes portable context.

## Overview
Running open-source/open-weight AI models ((and even proprietary models) in a local, private, and sometimes portable context offer significant advantages in security, efficiency, and accessibility. Running AI locally ensures that sensitive data stays private, reducing reliance on cloud services, and mitigating risks associated with data breaches. Running AI locally can also sometimes result in faster response times by eliminating network latency, making them ideal for real-time applications. Additionally, if the models are wrapped together with all the necessary dependencies to become truly portable, they can run on various devices, from laptops to mobile phones, enabling AI-powered solutions even in low-connectivity environments. In short, local AI gives users greater control and flexibility when working in both personal and enterprise environments regardless of whether they are online or offline.

## Advantages of Local AI
Local AI addresses several of common concerns about AI in general:

- **Fewer Hallucinations**  
  Local models can be fine-tuned on curated, domain-specific data, potentially reducing the likelihood of hallucinations and ensuring outputs align better with user intent.  

- **Increased Privacy and Consent**  
  Since data never leaves the local machine, privacy risks are minimized. Users can train models on datasets they legally own or have permission to use, avoiding ethical concerns around data scraping.  

- **Reduced Bias**  
  With full access to model weights and training data (for pre-training and/or post-training), developers can audit and modify biases rather than relying on opaque, corporate-controlled AI systems.  

- **Sustainable Deployment**  
  While training large models still requires resources, running (and potentially training) smaller, efficient models locally can be cost-effective and energy-efficient, reducing dependence on cloud computing.  

- **Improved Security**  
  Running AI in a private setting eliminates the risk of data exposure through cloud services.  

## Getting Started with Local AI

### DeepSeek-R1 and other open source/open weight models

DeepSeek-R1 is an open-source large language model designed to excel in complex reasoning tasks across various domains, including mathematics, coding, and logical inference. This makes it an excellent model to download and star experiment with in a local context. 

  ![Screenshot of DeepSeek paper](/images/deepseek_paper.png)

Key features include:

- **Reinforcement Learning-Based Training**: Utilizes large-scale reinforcement learning to develop advanced reasoning capabilities, further enhanced through supervised fine-tuning for improved readability and coherence.  [oai_citation_attribution:0‡build.nvidia.com](https://build.nvidia.com/deepseek-ai/deepseek-r1/modelcard?utm_source=chatgpt.com)

- **High Performance in Reasoning Benchmarks**: Demonstrates state-of-the-art results in various benchmarks, showcasing proficiency in logical inference, chain-of-thought reasoning, and real-time decision-making.  [oai_citation_attribution:1‡fireworks.ai](https://fireworks.ai/blog/deepseek-r1-deepdive?utm_source=chatgpt.com)

  ![Screenshot of DeepSeek performance](/images/deepseek_performance.png)

- **Open-Weight Accessibility**: Released under the MIT license, allowing full transparency and customization, enabling the community to leverage model weights and outputs for fine-tuning and distillation.  [oai_citation_attribution:2‡api-docs.deepseek.com](https://api-docs.deepseek.com/news/news250120?utm_source=chatgpt.com)

- **Cost-Effective Operation**: Developed at a fraction of the cost compared to other models, utilizing fewer chips and energy, challenging the traditional approach of expensive and energy-intensive AI infrastructures.  [oai_citation_attribution:3‡reuters.com](https://www.reuters.com/sustainability/sustainable-finance-reporting/esg-watch-deepseek-poses-deep-questions-about-how-ai-will-develop-2025-02-10/?utm_source=chatgpt.com)



In the sections below, DeepSeek-R1 will be used as an example, but the steps should be repeatable with any other open-source/open-weight model.

### Using Hugging Face to learn about the latest open-source/open-weight models
[Hugging Face](https://huggingface.co/) is a leading platform for exploring, developing, and sharing open-source AI models. It provides a vast repository of pre-trained models across various domains, including natural language processing, computer vision, and audio processing. By browsing the [**Models**](https://huggingface.co/models) hub, you can find the latest open-weight models and compare their performance. The platform also offers [**datasets**](https://huggingface.co/datasets) and other resources, making it an essential resource for researchers, developers, and AI enthusiasts. 
https://huggingface.co/models

  ![Screenshot of Hugging Face home](/images/hugging_face_main_page.png)

In theory, you can also use Hugging Face libraries to download and run AI models locally. However, beginners to local AI are likely to find this challenging for two main reasons:
- **Information on model sizes is not immediately clear**<br>
  This means that you may attempt to download a model that is too big to fit into the RAM of your local computer and will not work.

- **Code to run the models locally can be out-of-date**<br>
This means that when you attempt to download and run the model, the code throws an error or doesn't produce any output.

The solution is to use a more user-friendly interface to locate, download, and run AI models.

### Using LM Studio to discover, download, and run local LLMs

LM Studio is a powerful desktop application that allows users to run and experiment with large language models (LLMs) locally. It provides an intuitive interface for downloading, managing, and running open-weight models without requiring complex setup. Key features include **built-in model discovery**, **one-click downloads**, and **GPU acceleration support** for optimized performance. LM Studio also offers a **chat interface** for interacting with models and supports **customizable prompts** and parameters, making it ideal for both casual users and developers.

  ![Screenshot of LM Studio website](/images/lmstudio_home.png)

- **Step 1**
  Use the "Search" tab to display the "Mission Control" window, where you can search for a model and download it. Trending models will be listed and models that are likely to not fit on your local computer hardware will be flagged.

  ![Screenshot of LM Studio search](/images/lmstudio_load.png)

- **Step 2**
  In the "Chat" tab, select the model at the top of the screen, type your prompt and begin chatting with the model!

  ![Screenshot of LM Studio chat](/images/lmstudio_chat_response.png)

- **Optional steps**
  Use the experimental Retrieval Augmented Generation (RAG) feature to add content from files into the context window of the model to query it.

  ![Screenshot of LM Studio rag](/images/lmstudio_rag.png)


### Using Ollama to Discover, Download, and Run Local LLMs

Ollama is a versatile tool that enables users to run and experiment with large language models (LLMs) locally. It offers a straightforward command-line interface for downloading, managing, and interacting with open-weight models without complex setups. Key features include **model discovery**, **simple model downloads**, and **customizable system prompts** to tailor model behavior. Ollama is suitable for both casual users and developers seeking to explore LLMs on their local machines.

  ![Screenshot of Ollama](/images/ollama_home.png)

- **Step 1**  
  Download and install Ollama from the [official website](https://ollama.com/). Choose the installer that matches your operating system—macOS, Linux, or Windows. After installation, open your command-line interface (CLI).

- **Step 2**  
  Find available models through the "Models" section of the Ollama website, where you can search for a model or choose one of the trending models that are listed.

    ![Screenshot of Ollama models](/images/ollama_deepseek_models.png)

- **Step 3**  
  Click on the model card to see details of the model. Here, you can also select which version of the model you want to download and run locally on your computer, and copy the exact command to paste into your local command line inteface (CLI)  (see Step 4) to get things working.

    ![Screenshot of Ollama r1](/images/ollama_deepseek_r1.png)

- **Step 4**  
  In your command line inteface (CLI) (CMD.exe on Windows or Terminal on MacOS), automatically pull the desired model from Hugging Face (if it's not already downloaded) and run the model, by executing the command:

  ```bash
  ollama run [model_name]
  ```

  Replace [model_name] with the specific model you wish to download, such as deekseek-R1:8b. This command downloads the model onto your machine.

  ```bash
  ollama run deekseek-R1:8b
  ```

  This will start an interactive session where you can input prompts and receive responses from the model.
  
    ![Screenshot of Ollama r1](/images/ollama_chat.png)

- **Step 3**  

  To exit the session, type /bye.

    ```bash
    > /bye
    ```

To be continued...
