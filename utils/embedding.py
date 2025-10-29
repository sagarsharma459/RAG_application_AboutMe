import requests
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()



def get_embedding(text):
    API_KEY = os.getenv("API_KEY")  # Use env var for security
    url = "https://api.euron.one/api/v1/euri/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
        
    }
    payload = {
        "input": text,
        "model": "text-embedding-3-small"
    }
    response = requests.post(url, headers=headers, json=payload)
    return np.array(response.json()['data'][0]['embedding'])



