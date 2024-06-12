from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = FastAPI()

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

class InferenceRequest(BaseModel):
    prompt: str
    max_length: int = 50
    num_return_sequences: int = 1

@app.post("/gpt2-inference/")
def gpt2_inference(request: InferenceRequest):
    inputs = tokenizer(request.prompt, return_tensors="pt")
    outputs = model.generate(
        inputs.input_ids,
        max_length=request.max_length,
        num_return_sequences=request.num_return_sequences
    )
    responses = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return {"responses": responses}

# To run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
