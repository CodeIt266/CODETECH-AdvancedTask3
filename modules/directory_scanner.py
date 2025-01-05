import requests

def scan_directories(target, directories):
    for dir in directories:
        url = f"{target}/{dir}"
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Found: {url}")