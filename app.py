import requests
url = "https://api.chess.com/pub/player/hikaru"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)



data = response.json()

# print(data)



