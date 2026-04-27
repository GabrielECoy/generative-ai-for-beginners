from openai import OpenAI
import base64

from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
response = client.images.generate(
        model="gpt-image-1",
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
        size='1024x1024',
        n=1)
with open("generated-image.png", "wb") as f: f.write(base64.b64decode(response.data[0].b64_json))

from PIL import Image
image = Image.open("generated-image.png")
image.show()