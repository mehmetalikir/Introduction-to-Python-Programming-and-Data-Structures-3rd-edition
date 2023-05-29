# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

''''''

import asyncio
import itertools
import time

import aiohttp

start = time.time()

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lengths = [2]

sequences = []

for length in lengths:
    sequences.extend([''.join(seq) for seq in itertools.product(characters, repeat=length)])

urls = []

for i in range(len(sequences)):
    url = f"https://media.pearsoncmg.com/intl/ge/2022/cws/ge_liang_ipp_3/cw/content/{sequences[i]}.zip"
    urls.append(url)


# Define an async function to send HTTP requests
async def send_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Do something with the response if needed
            if response.status == 200:
                print("THIS ", url, "IS ACTIVE")


# Create an event loop
loop = asyncio.get_event_loop()

# Gather all the requests and execute them concurrently
tasks = [send_request(url) for url in urls]
loop.run_until_complete(asyncio.gather(*tasks))

# Close the event loop
loop.close()

end = time.time()

print(end - start)
