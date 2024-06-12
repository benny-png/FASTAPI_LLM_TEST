
# FastAPI LLM Inference

This project demonstrates how to create an inference API using FastAPI and a pre-trained language model from Hugging Face's Transformers library. The API can generate text based on a given prompt using the GPT-2 model.


![Watch the video](https://github.com/benny-png/FASTAPI_LLM_TEST/blob/main/FASTAPI.gif)


## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **Transformers**: Utilize state-of-the-art NLP models from Hugging Face.
- **Uvicorn**: An ASGI server for serving the FastAPI application.
- **Nest-Asyncio**: Allows nested event loops in environments like Jupyter Notebooks.
- **Pyngrok**: Exposes the local server to the internet for external access.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Transformers
- Torch
- Requests
- Nest-Asyncio
- Pyngrok

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/FASTAPI_LLM_TEST.git
    cd FASTAPI_LLM_TEST
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the FastAPI Application Locally

1. Start the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

2. (Optional) Expose the local server to the internet using ngrok:
    ```bash
    ngrok http 8000
    ```

### Making a POST Request

You can test the API using tools like cURL, Postman, or directly from a Python script.

#### Using cURL

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/gpt2-inference/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Once upon a time",
  "max_length": 50,
  "num_return_sequences": 1
}'
```

#### Using Python

```python
import requests
import json

# Define the endpoint URL
url = "http://127.0.0.1:8000/gpt2-inference/"  # Replace with the ngrok URL if using ngrok

# Create the payload for the request
payload = {
    "prompt": "Once upon a time",
    "max_length": 50,
    "num_return_sequences": 1
}

# Send the POST request to the FastAPI endpoint
response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})

# Print the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Failed to get response. Status code:", response.status_code)
```

#### Using Postman

1. Open Postman and create a new POST request.
2. Set the URL to `http://127.0.0.1:8000/gpt2-inference/` (or your ngrok URL).
3. Set the request body to raw JSON and enter the following:
    ```json
    {
      "prompt": "Once upon a time",
      "max_length": 50,
      "num_return_sequences": 1
    }
    ```
4. Send the request and view the response.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```


