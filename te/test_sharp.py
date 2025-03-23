import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("SERPER_API_KEY"))
SERPER_API_KEY = os.getenv("SERPER_API_KEY")  # Get API key

if not SERPER_API_KEY:
    print("API Key is missing! Set SERPER_API_KEY before running.")
else:
    url = "https://google.serper.dev/search"
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'content-type': 'application/json'
    }
    payload = json.dumps({"q": "best cities for foodies in May 2025"})

    response = requests.post(url, headers=headers, data=payload)

    print(f"Status Code: {response.status_code}")
    print("Response:", response.json())

