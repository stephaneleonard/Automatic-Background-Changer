"""Resize the image and add text to it"""
from PIL import Image, ImageDraw, ImageFont

def add_context(text):
    """add text to image"""
    image = Image.open('sample_image.png')
    width, _ = image.size
    draw = ImageDraw.Draw(image)
    fnt = ImageFont.truetype('Roboto-Bold.ttf', 25)
    draw.text((width / 2, 200), text, fill=(255, 255, 255), font=fnt)
    image.save('sample_image.png')
