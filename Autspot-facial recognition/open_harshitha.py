import urllib.request
import openai
import urllib.request
from PIL import Image

openai.api_key = "API_KEY"
def gen_image(promt_text):
  response = openai.Image.create(
    prompt=promt_text,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  return image_url
  # urllib.request.urlretrieve(image_url, "calmscenery.png")
  # img = Image.open("calmscenery.png")
  # img.show()
