# Real Example 
# File downloading

import threading
import time
import requests


# python3 -m venv venv
# source venv/bin/activate
# pip install --upgrade pip
# pip install requests

def download(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished downloading from {url},size: {len(response.content)} bytes")


urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png"
    "https://httpbin.org/image/svg"
]



start = time.time()
threadsTemp = []

for url in urls:
    t = threading.Thread(target=download,args=(url,))
    t.start()
    threadsTemp.append(t)

#Wait to complete
for t in threadsTemp:
    t.join()

end = time.time()



print(f"All downloads done in {end - start:.2f} seconds")

# we will use threads for i/o bound operation
# example: disk read/write/ web requests


# This sends an HTTP request to the website.

# Now something important happens...

# Python is waiting.

# The internet takes some time.

# Maybe

# 0.2 seconds
# 1 second
# 3 seconds

# CPU isn't doing much.

# It is simply waiting for data.

# This is called an I/O-bound operation