import requests as rq
import os
from ccwc import ccwc

url = 'https://www.gutenberg.org/cache/epub/132/pg132.txt'
save_path = './unix-wc-command/input/test.txt'

def download_source_file(url, save_path):
    response = rq.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded and saved to {save_path}")
    else:
        print("Failed to download the file")

# download_source_file(url, save_path)
ccwc.run()