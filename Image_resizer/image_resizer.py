from PIL import Image,ImageDraw, ImageFont


def resize_image(width, height, text):
    image = Image.open('sample_image.png')
    image.thumbnail([width, height])
    d = ImageDraw.Draw(image)
    fnt = ImageFont.truetype('Roboto-Bold.ttf', 25)
    d.text((width / 2,200), text, fill=(255,255,255), font=fnt)
    image.save('sample_image.png')