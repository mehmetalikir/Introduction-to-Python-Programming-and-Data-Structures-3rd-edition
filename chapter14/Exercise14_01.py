# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

''''''

import itertools
import time
from concurrent.futures import ThreadPoolExecutor

import requests

start = time.time()

# Define the number of concurrent requests you want to send
concurrency = 10

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lengths = [3]

sequences = []

for length in lengths:
    sequences.extend([''.join(seq) for seq in itertools.product(characters, repeat=length)])

urls = []

for i in range(len(sequences)):
    url = f"https://media.pearsoncmg.com/intl/ge/2022/cws/ge_liang_ipp_3/cw/content/{sequences[i]}.zip"
    urls.append(url)


# Function to send HTTP requests
def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("THIS", url, "IS ACTIVE.")


# Create a ThreadPoolExecutor to manage the concurrent requests
with ThreadPoolExecutor(max_workers=concurrency) as executor:
    # Submit each URL to the executor
    # This will start sending requests concurrently
    executor.map(send_request, urls)

end = time.time()

print(end - start)
