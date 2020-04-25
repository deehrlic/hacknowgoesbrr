#TAKES ARG THAT IS MONGO KEY
# from databasemachine import getLink
from PIL import Image, ImageDraw, ImageFont
import urllib.request
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
    font = ImageFont.truetype("arial.ttf", 12)

    #GET MONGO_VERBOSE
    verbose = verbose.replace("_"," ")
    verbose = verbose.replace("! ","! \n")
    verbose = verbose.replace("ing ma","ing \nma")
    print(verbose)
    d.text((40,210), verbose, fill=(0,0,0), font=font)

    #rightguy uses mongo_key
    font = ImageFont.truetype("arial.ttf", 20)
    d.text((300,210), "haha "+key[:20]+" go brrrr", fill=(0,0,0), font=font)

    path = "static/"+key.replace(" ","")+".jpg"
    urllib.request.urlretrieve(link, path)

    wiki = Image.open(path)
    w1 = wiki.resize((120,120))
    img.paste(w1, (280,40))


    img.save('go_brr.png')
