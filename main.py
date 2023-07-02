# -------------------------#
# StockX360 GIF Generator  #
# Author: Christian Cheng  #
# GitHub: christiancheng15 #
# -------------------------#

import requests
from bs4 import BeautifulSoup
import json
import imageio.v2 as imageio
from art import *
import re
import os

def menu():
    # Menu
    tprint("StockX360")
    print("Usage:")
    print("1. Input StockX link e.g. https://stockx.com/nike-dunk-low-retro-white-black-2021")
    print("2. Press ENTER to generate GIF")
    print("Note: Not all products have 360° images. It may take upwards of 30 seconds. Enter Q/q to quit.\n")


def create_gif():
    # User enter StockX link e.g. https://stockx.com/nike-dunk-low-retro-white-black-2021
    while True:
        url = input("StockX Link: ")

        if url.lower() == "q":
            quit()

        # Validate StockX link format https://stockx.com/...
        # 1. Validate regex
        pattern = r"^https:\/\/stockx\.com\/[a-zA-Z0-9-]+$"
        if re.match(pattern, url):
            #Validate url exists
            response = requests.get(url)
            if response.status_code == 200:
                break
        print("Error. Please enter a valid StockX link. https://stockx.com/...")

    # Parse HTML page and scrape images
    soup = BeautifulSoup(response.content, "html.parser")
    next_data = soup.find("script", id="__NEXT_DATA__", type="application/json").text
    next_data_json = json.loads(next_data)
    queries = next_data_json["props"]["pageProps"]["req"]["appContext"]["states"]["query"]["value"]["queries"]

    # 2/7 - Add try/except to parse all_360_images as each product has different "queries" length
    for num in range(0,len(queries)):
        try:
            all_360_images = queries[num]["state"]["data"]["product"]["media"]["all360Images"]
        except:
            pass

    images = [imageio.imread(requests.get(url).content) for url in all_360_images]

    # Format file name
    file_name = url.replace("https://stockx.com/", "") + ".gif"

    # Check if images contains images. Yes - Create GIF / No - Exit
    if images:
        imageio.mimsave(file_name, images, duration=0, loop=0)
        print(f"{file_name} created successfully.")
    else:
        print("No images were successfully loaded to create the GIF.")

menu()
while True:
    create_gif()
