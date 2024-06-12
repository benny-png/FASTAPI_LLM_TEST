import requests
import json

# Define the endpoint URL
url = "https://557c-41-86-177-7.ngrok-free.app/gpt2-inference/"

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
