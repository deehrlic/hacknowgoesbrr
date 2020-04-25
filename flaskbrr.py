from flask import Flask, render_template, request, send_file
import re
import requests
#from bs4 import BeautifulSoup
import wikipedia, random
import urllib.request
from pymongo import MongoClient
from databasemachine import upsertDB

app = Flask(__name__)
client = MongoClient("mongodb+srv://machinego:machinego123@mememachine-dopfr.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
db = client.get_database('ImageSource')
src = db.source 

@app.route("/")
def home():
    print(src.count_documents({}))
    memes = list(src.find())
    print(memes)
    print(len(memes))
    return render_template("frontpage.html")

@app.route("/parse", methods=['GET', 'POST'])
def parse():
    if request.method == "POST":

        #make verbose
        #you cant just make -synonym/hypernym- machine go brrrrr
        verbose = "NOOOOOOOOOOOOOOO!!! You can't just make " + request.form['user_i'] + " go brrrrr!"


        #get image from wikipedia and save to computer
        res = wikipedia.search(request.form['user_i'])
        img = ""
        if len(res) > 0:
            try:
                img = wikipedia.page(res[0]).images[0]
                print(img)
                path = "static/"+res[0].replace(" ","")+".jpg"

            except wikipedia.DisambiguationError as e:
                img = wikipedia.page(e.options[0]).images[0]
                print(img)
                path = "static/"+e.options[0].replace(" ","")+".jpg"

            urllib.request.urlretrieve(img, path)

                #SEND TO MONGO
                #request.form['user_i'] = input term
                #verbose = verbose form of term
                #img = the link to image to be displayed
            upsertDB(request.form['user_i'], img, verbose, src)

            #change to PIL image
            return send_file(path, mimetype='image')


        #THIS MEANS SEARCH FAILED BRO
        else:
            return 'sdfsdfds'







        return verbose


        #get image
        #send to mongo
        #assemble image

if __name__ == "__main__":
    app.run(debug=True)

