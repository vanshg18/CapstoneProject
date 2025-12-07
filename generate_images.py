import os
import requests
from PIL import Image
from io import BytesIO
import numpy as np

def fetch_and_store_image(image_url, destination, index, total_count):
    """Download an image with retries and save it to disk."""
    for retry in range(1, 4):
        print(f"Fetching image {index}/{total_count} (Attempt {retry}/3)...")
        try:
            headers = {'User-Agent': 'RandomImageCollector/1.0'}
            resp = requests.get(image_url, headers=headers, timeout=15)

            if resp.status_code == 200:
                with Image.open(BytesIO(resp.content)) as pic:
                    pic.save(destination)
                print(f"Saved image {index}/{total_count} -> {destination}\n")
                return True
            else:
                print(f"Download failed for image {index}/{total_count}: HTTP {resp.status_code}")
        except Exception as err:
            print(f"Attempt {retry} failed for image {index}/{total_count}: {err}")

    print(f"Giving up on image {index}/{total_count} after 3 failed attempts.\n")
    return False


def create_image_dataset(directory='input', count=20):
    """Create a folder and populate it with random images from Picsum."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"New directory created: {directory}")
    else:
        for existing_file in os.listdir(directory):
            os.remove(os.path.join(directory, existing_file))
        print(f"Cleaned up existing files in {directory}")

    for num in range(1, count + 1):
        random_seed = np.random.randint(1_000_000)
        image_url = f"https://picsum.photos/seed/{random_seed}/512/512"
        file_path = os.path.join(directory, f"image_{num}.jpg")
        fetch_and_store_image(image_url, file_path, num, count)


if __name__ == '__main__':
    create_image_dataset()
