from flask import Flask, render_template, request, send_file
import re
import requests
#from bs4 import BeautifulSoup
import wikipedia, random
import urllib.request
from pymongo import MongoClient
from databasemachine import upsertDB, connect, getRandomSrc
import makeimage
from nltk.corpus import wordnet
from random import randrange

app = Flask(__name__)
src = connect()

@app.route("/")
def home():
    item = getRandomSrc(src)
    search = item["search"]
    link = item["link"]
    verbose = item["verbose"]
    return render_template("frontpage.html")

@app.route("/parse", methods=['GET', 'POST'])
def parse():
    if request.method == "POST":

        #make verbose
        verbo = request.form['user_i']

        if verbo == "money printer":
            return send_file('original_meme.png', mimetype='image')


        verbose = "NOOOOOOOOOO" + '!'*randrange(5,8) + " You can't just make " + verbo + " go brrrrr!"
        #you cant just make -synonym/hypernym- machine go brrrrr






        #get image from wikipedia and save to computer
        res = wikipedia.search(request.form['user_i'])
        img = ""
        if len(res) > 0:


            if len(wordnet.synsets(verbo)) > 0:
                syn = wordnet.synsets(request.form['user_i'])[0]
                lemmas = syn.lemmas()
                if len(syn.lemmas()) > 1:
                    if lemmas[0].name() == verbo:
                        verbo = lemmas[1].name()
                    else:
                        verbo = lemmas[0].name()
                    print(verbo)
                    verbo.replace("_"," ")
                    verbose = "NOOOOOOOOOO" + '!'*randrange(5,8) + " You can't just make " + verbo + "ing machine go brrrrr!"
                    print(verbose)

            print(verbose)



            try:
                imgs = [i for i in wikipedia.page(res[0]).images if i.endswith(".jpg")]
                print(imgs)
                if len(imgs)>0:
                    img = imgs[0]
                    print(img)
                    path = "static/"+request.form['user_i'].replace(" ","")+".jpg"
                    urllib.request.urlretrieve(img, path)
                else:
                    return send_file('404page.png', mimetype='image')

            except wikipedia.DisambiguationError as e:
                chosen = e.options[0]
                if chosen == request.form['user_i']:
                    chosen= e.options[1]
                imgs = [i for i in wikipedia.page(chosen).images if i.endswith(".jpg")]
                if len(imgs) > 0:
                    img = imgs[0]
                    print(img)
                    path = "static/"+chosen.replace(" ","")+".jpg"
                    urllib.request.urlretrieve(img, path)
                else:
                    return send_file('404page.png', mimetype='image')



                #SEND TO MONGO
                #request.form['user_i'] = input term
                #verbose = verbose form of term
                #img = the link to image to be displayed
            upsertDB(request.form['user_i'], img, verbose, src)

            img = makeimage.makeImage(request.form['user_i'], src)

            #change to PIL image
            #return send_file(path, mimetype='image')
            return send_file('go_brr.png', mimetype='image')


        #THIS MEANS SEARCH FAILED BRO
        else:
            return send_file('404page.png', mimetype='image')




if __name__ == "__main__":
    app.run(debug=True)
