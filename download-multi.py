import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor

def download_file(url, save_folder):
    local_filename = os.path.join(save_folder, url.split('/')[-1])
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
        print(f'Downloaded file: {local_filename}')
    except Exception as e:
        print(f'Error while downloading {url}: {e}')

def main():
    file_with_urls = 'cloudinary_urls.txt'  # TXT with URLs
    save_folder = 'downloaded_files'  # Dir where you want your files downloaded
    max_threads = 5  # Number of threads

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    urls = []
    with open(file_with_urls, 'r') as file:
        urls = [url.strip() for url in file if url.strip()]

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for url in urls:
            executor.submit(download_file, url, save_folder)
            time.sleep(0.5)  # 0.5 second pause between starting threads to avoid spamming API

if __name__ == "__main__":
    main()
