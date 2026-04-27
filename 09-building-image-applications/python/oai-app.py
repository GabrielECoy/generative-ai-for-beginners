from openai import OpenAI
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()
 
client = OpenAI()


try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        model="dall-e-3", # "gpt-image-1" does not support url response
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=1
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    print(str(generation_response)[:40])

    image_url = generation_response.data[0].url # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    # gpt-image-1 returns base64-encoded image data (b64_json) by default rather than a URL, so there's no need to make a separate requests.get() call to download it.
    # Decoding: You decode the base64 string with base64.b64decode() to get the raw image bytes before writing to disk.
    # import base64
    # image_data = generation_response.data[0].b64_json  # extract base64 image data
    # generated_image = base64.b64decode(image_data)
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except OpenAI.InvalidRequestError as err:
    print(err)

# ---creating variation below---

# failed with 502 or openai.APIConnectionError: Connection error.
response = client.images.create_variation(
  image=open(image_path, "rb"),
  n=1,
  size="1024x1024"
)
