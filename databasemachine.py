
from pymongo import MongoClient

#conect to db and return cluster thing
def connect():
    client = MongoClient("mongodb+srv://machinego:machinego123@mememachine-dopfr.gcp.mongodb.net/test?retryWrites=true&w=majority")
    db = client.test
    db = client.get_database('ImageSource')
    src = db.source
    return src


def upsertDB(search, link, verbose, src):
    if not list(src.find({"search": search})):
        print("upsert!")
        db_update = {
            "search": search,
            "link": link,
            "verbose": verbose
        }
        src.insert(db_update)
    else:
        print("don't do it!")

# def getLink(key):




# client = MongoClient("mongodb+srv://machinego:machinego123@mememachine-dopfr.gcp.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test

# db = client.get_database('ImageSource')
# src = db.source 



