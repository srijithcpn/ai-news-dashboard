import requests

API_KEY = "be6993db868843b08ef47b738b99fdb1"

url = (
    f"https://newsapi.org/v2/everything?"
    f"q=artificial intelligence&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"apiKey={API_KEY}"
)

response = requests.get(url)

print(response.status_code)
print(response.json())