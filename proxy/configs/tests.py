import requests

if __name__ == "__main__":
    response = requests.get("https://albertazemar.com")
    print(response.content)
