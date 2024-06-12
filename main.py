import requests
def main():
  places = [
    'svo', 
    'paris', 
    'cherepovec'
  ]
  payload = {
    "MnTqQ": "", 
    "lang": "ru"
  }
  for place in places:
    response = requests.get(f"https://wttr.in/{place}", params = payload)
    print(response.text)
if __name__ == "__main__":
  main()


