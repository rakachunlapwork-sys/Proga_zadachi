import requests

def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False

def main():
    url = "https://swapi.dev/api/starships/?search=Millenium_Falcon"
    data = send_request(url)
    pilots = data["pilots"]

    for c in pilots:
        pilot_name = send_request(c)
        print(f"- {pilot_name}")
if __name__ == "__main__":
    main()