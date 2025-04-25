import os
from dotenv import load_dotenv
import requests
from .models import NationalPark, ParkPhoto

load_dotenv()

API_KEY = os.getenv("NATIONAL_PARKS_API_KEY")
BASE_URL = "https://developer.nps.gov/api/v1/parks"


def import_parks():
    params = {
        "api_key": API_KEY,
        "limit": 75,  # Load a lot of parks at once
        "designation": "National Park",
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print("Failed to fetch data from NPS API")
        return

    data = response.json().get("data", [])

    for park_data in data:
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

        for image in images:
            ParkPhoto.objects.create(
                park=park, image_url=image.get("url"), alt_text=image.get("altText", "")
            )

    print(f"Imported {len(data)} parks!")
