import requests

def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return False

def main():
    url = "https://swapi.dev/api/people/1/"
    data = send_request(url)
    get_data = data["homeworld"]

    url2 = get_data
    data2 = send_request(url2)
    homeworld = data2["name"]
    print(f'Люк Скайуокер родился на планете {homeworld}')

if __name__ == "__main__":
    main()