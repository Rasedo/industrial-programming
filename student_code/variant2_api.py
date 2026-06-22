import requests, json, time
url = "https://api.example.com/data"
while True:
    try:
        r = requests.get(url)
        data = json.loads(r.text)
        print("Got data:", data)
    except Exception:
        pass
    time.sleep(5)
