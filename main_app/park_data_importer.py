import os
from dotenv import load_dotenv
import requests
from .models import NationalPark, ParkPhoto

load_dotenv()

API_KEY = os.getenv("NATIONAL_PARKS_API_KEY")
BASE_URL = "https://developer.nps.gov/api/v1/parks"

OFFICIAL_NATIONAL_PARK_CODES = [
    "acad",
    "arch",
    "badl",
    "bibe",
    "bisc",
    "blca",
    "brca",
    "cany",
    "care",
    "cave",
    "chan",
    "choh",
    "cong",
    "crla",
    "cuga",
    "cuva",
    "deva",
    "dena",
    "drto",
    "ever",
    "gaar",
    "glac",
    "grba",
    "grca",
    "grsa",
    "grsm",
    "gumo",
    "hale",
    "havo",
    "hosp",
    "indu",
    "isro",
    "jotr",
    "katm",
    "kefj",
    "kova",
    "lacl",
    "lavo",
    "maca",
    "meve",
    "mora",
    "noca",
    "olym",
    "pefo",
    "pinn",
    "redw",
    "romo",
    "sagu",
    "seki",
    "shen",
    "thro",
    "viis",
    "voyg",
    "whsa",
    "wica",
    "wrst",
    "yell",
    "yose",
    "zion",
    "amis",
    "care",
    "jotr",
    "katm",
    "kefj",
    "lacl",
    "wrst",
    "gaar",
]


def import_parks():
    params = {
        "api_key": API_KEY,
        "limit": 500,  # Load a lot of parks at once
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print("Failed to fetch data from NPS API")
        return

    data = response.json().get("data", [])
    parks_imported = 0
    photos_imported = 0

    for park_data in data:
        if park_data.get("parkCode") not in OFFICIAL_NATIONAL_PARK_CODES:
            continue

        full_name = park_data.get("fullName")
        states = park_data.get("states")
        description = park_data.get("description")
        url = park_data.get("url")
        images = park_data.get("images", [])
        photo_url = images[0]["url"] if images else ""

        # Create or update the NationalPark
        park, created = NationalPark.objects.update_or_create(
            name=full_name,
            defaults={
                "location": states,
                "description": description,
                "website": url,
                "photo_url": photo_url,
            },
        )

        if not created:
            park.photos.all().delete()

        for index, image in enumerate(images):
            if index >= 5:
                break

            ParkPhoto.objects.create(
                park=park, image_url=image.get("url"), alt_text=image.get("altText", "")
            )
            photos_imported += 1

        parks_imported += 1

    print(f"Imported {parks_imported} parks!")
    print(f"Imported {photos_imported} photos!")
