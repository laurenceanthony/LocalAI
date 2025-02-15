import requests
import json

# Define the API endpoint (check LMStudio settings for the correct port)
API_URL = "http://localhost:1234/v1/completions"

# Define the request payload with streaming enabled
payload = {
    # "model": "llama-3.2-1b-instruct",
    "model": "lmstudio-community/deepseek-r1-distill-llama-8b",
    "prompt": "What is the capital of France?",
    "temperature": 0.6,
    "stream": True  # Enable streaming
}

# Send the request with stream=True
response = requests.post(API_URL, json=payload, stream=True)

# Check if the request was successful
if response.status_code == 200:
    print("Response:")
    for line in response.iter_lines():
        if line:
            # Decode the line and parse JSON
            decoded_line = line.decode("utf-8")
            # Streaming responses start with 'data: '
            if decoded_line.startswith("data: "):
                decoded_line = decoded_line[6:]  # Remove 'data: ' prefix
            try:
                json_data = json.loads(decoded_line)
                print(json_data.get("choices", [{}])[
                      0].get("text", ""), end="", flush=True)
            except json.JSONDecodeError:
                pass  # Ignore invalid JSON lines
else:
    print("Error:", response.status_code, response.text)
