This script is made because Cloudinary doesn't allow downloading all resources at once without going through huge hassle of endless documentation and API calls.

It will get all of your Cloudinary resources as URLs, save them, and allow you to download them all at once.

_resource-scraper.py_ will get all of your URLs and save them to **cloudinary_urls.txt**.
To make it work, you will have to enter your cloud name, API key and API secret.

_download.py_ will get URLs from _cloudinary_urls.txt_ and download them to folder **downloaded_files**.

_download-multi.py_ is same as _download.py_, just multi threaded.

Have fun :)
