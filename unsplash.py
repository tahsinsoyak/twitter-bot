from typing import List
import requests as requests
import os as os
import random as random
import dotenv as dotenv
import constants as constants

dotenv.load_dotenv()

ACCESS_KEY = os.environ["ACCESS_KEY"]


def _search_images() -> List:
    query = random.choice(constants.UNSPLASH_QUERIES)
    url = f"https://api.unsplash.com/search/photos?page=1&query={query}&client_id={ACCESS_KEY}"
    response = requests.get(url)

    data = response.json()["results"]
    return data

def _get_rand_image_link():
    response_data = _search_images()
    random_image_data = random.choice(response_data)

    link = random_image_data["urls"]["regular"]
    return link


def download_image():
    filename = "picture.jpg"
    image_url = _get_rand_image_link()
    image_response = requests.get(image_url,stream=True)
    if image_response.status_code == 200:
        with open(filename,"wb") as image_file:
            for chunk in image_response:
                image_file.write(chunk)

