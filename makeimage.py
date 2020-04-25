#TAKES ARG THAT IS MONGO KEY
# from databasemachine import getLink
from PIL import Image, ImageDraw, ImageFont

def makeImage(key, src):

    #GET MONGO INFO
    item = src.find_one({"search" : key})
    print(type(item))
    search = key
    verbose = item["verbose"]
    link = item["link"]


    img = Image.new('RGB', (600, 300), color = 'white')

    leftguy = Image.open('leftguy.png')
    rightguy = Image.open('rightguy.png')

    img.paste(leftguy, (30,30))
    img.paste(rightguy, (380,30))


    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 20)

    #GET MONGO_VERBOSE
    d.text((80,210), "left guy text", fill=(0,0,0), font=font)

    #rightguy uses mongo_key
    d.text((300,210), "haha "+key[:18]+" go brrrr", fill=(0,0,0), font=font)

    #####ADDD WIKKIIIII IMAGE#############

    img.save('go_brr.png')
