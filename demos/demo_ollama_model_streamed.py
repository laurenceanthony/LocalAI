import ollama


def main():
    # model = "llama3.2"
    model = "deepseek-r1:8b"
    prompt = "What is the capital of France?"
    # Stream the response
    for chunk in ollama.chat(model=model, messages=[{"role": "user", "content": prompt}], stream=True):
        print(chunk["message"]["content"], end="", flush=True)

    print()  # Newline after response


if __name__ == "__main__":
    main()
