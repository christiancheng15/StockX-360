import argparse
import requests
from bs4 import BeautifulSoup
import json
import imageio
import re
import os

def scrape_images(url):
    print(f"Scraping images from {url}...")
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        next_data = soup.find("script", id="__NEXT_DATA__", type="application/json").text
        next_data_json = json.loads(next_data)
        queries = next_data_json["props"]["pageProps"]["req"]["appContext"]["states"]["query"]["value"]["queries"]
        for i in range(len(queries)):
            try:
                images = queries[i]["state"]["data"]["product"]["media"]["all360Images"]
                print(images)
                return images
            except:
                pass
    else:
        print("Faled to retrive data from the URL.")
        return []

def generate_gif(clockwise, images, output_path):
    
    if clockwise:
        images = images[::-1]

    cleaned_image_urls = [re.sub(r'\?.*$', '', url) for url in images]

    print(f"Generating {output_path}")
    with imageio.get_writer(output_path, mode='I') as writer:
        for image_url in cleaned_image_urls:
            response = requests.get(image_url)
            image = imageio.imread(response.content)
            writer.append_data(image)
    print("GIF generated successfully!")

def main():
    parser = argparse.ArgumentParser(description="Generate a 360-degree GIF of a sneaker from StockX.")
    parser.add_argument('--url', type=str, required=True, help='URL of the StockX sneaker page with a 360-degree view.')
    parser.add_argument('--clockwise', type=int, choices=[0,1], default=1, required=False, help='Set to 1 for clockwise rotation, 0 for counterclockwise rotation.')
    args = parser.parse_args()
    url = args.url
    clockwise = args.clockwise
    images = scrape_images(url)

    if not images:
        print("No images were scraped. Exiting...")
        return
    
    sneaker_name = url.split('/')[-1]
    output_path = os.path.join('output', f'{sneaker_name}.gif')

    generate_gif(clockwise, images, output_path)

if __name__ == "__main__":
    main()
