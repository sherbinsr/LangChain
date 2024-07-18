from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint

# Load environment variables from the .env file
load_dotenv()

# Access the Hugging Face API token
huggingface_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Check if the token is loaded correctly
if huggingface_api_token is None:
    raise ValueError("Hugging Face API token is not set. Please check your .env file.")

# Initialize the endpoint with explicit parameters and the API token
llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-large",
    temperature=0.6,
    model_kwargs={"max_length": 64},
    huggingfacehub_api_token=huggingface_api_token
)

# Use the endpoint with invoke
try:
    response = llm.invoke("what is the capital of India")
    print(response)
except Exception as e:
    print(f"Error invoking the model: {e}")
