
from pymongo import MongoClient
import random

#conect to db and return cluster thing
def connect():
    client = MongoClient("mongodb+srv://machinego:machinego123@mememachine-dopfr.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    db = client.get_database('ImageSource')
    src = db.source
    return src

#insert new search intodb
def upsertDB(search, link, verbose, sound, src):
    if not list(src.find({"search": search, "sound": sound)):
        print("upsert!")
        db_update = {
            "search": search,
            "link": link,
            "verbose": verbose,
            "sound": sound
        }
        src.insert(db_update)
    else:
        print("don't do it!")

# get random source
def getRandomSrc(src):
    res = list(src.find({}))
    return res[random.randint(0, len(res) - 1)]




# client = MongoClient("mongodb+srv://machinego:machinego123@mememachine-dopfr.gcp.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test

# db = client.get_database('ImageSource')
# src = db.source 



