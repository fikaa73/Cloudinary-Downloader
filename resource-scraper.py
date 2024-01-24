import requests
from requests.auth import HTTPBasicAuth
import time

def fetch_cloudinary_resources(username, password, next_cursor=None):
    
    cloud_name = 'x' #YOUR CLOUD NAME
    api_url = 'https://api.cloudinary.com/v1_1/' + cloud_name + '/resources/search'
    params = {'next_cursor': next_cursor} if next_cursor else {}

    response = requests.get(api_url, params=params, auth=HTTPBasicAuth(username, password))
    if response.ok:
        return response.json()
    else:
        raise Exception(f'Request error: {response.status_code}')

def save_secure_urls(urls, file_path):
    with open(file_path, 'a') as file:
        for url in urls:
            file.write(url + '\n')

def main():
    username = 'x' #API_KEY
    password = 'x' #API_SECRET
    next_cursor = None
    file_path = 'cloudinary_urls.txt'
    i=0

    while True:
        data = fetch_cloudinary_resources(username, password, next_cursor)
        secure_urls = [resource['secure_url'] for resource in data['resources']]
        save_secure_urls(secure_urls, file_path)

        next_cursor = data.get('next_cursor')
        i=i+1
        print(f"Pass {i}")
        print(next_cursor)
        if not next_cursor:
            print("Done!")
            break

        time.sleep(1)  # 1 second pause between requests to avoid spamming API

if __name__ == "__main__":
    main()
