import requests
import time
import os

def download_file(url, save_folder):
    local_filename = os.path.join(save_folder, url.split('/')[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def main():
    file_with_urls = 'cloudinary_urls.txt'  # TXT with URLs
    save_folder = 'downloaded_files'  # Dir where you want your files downloaded

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(file_with_urls, 'r') as file:
        for url in file:
            url = url.strip()
            if url:
                print(f'Downloaded file: {url}')
                download_file(url, save_folder)
                time.sleep(0.5)  # 0.5 second pause between requests to avoid spamming API

if __name__ == "__main__":
    main()
