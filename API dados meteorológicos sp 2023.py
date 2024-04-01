import requests
import json

url = "https://history.openweathermap.org/data/2.5/aggregated/year?lat=-23.5505&lon=-46.6333&appid=8558f2c4b75140b6e09bedb89a5a4aec"

resposta = requests.get(url)

print(json.loads(resposta.text))
