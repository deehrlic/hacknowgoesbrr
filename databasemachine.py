
from pymongo import MongoClient


def upsertDB(search, link, verbose, src):
    db_update = {
        "search": search,
        "link": link,
        "verbose": verbose
    }
    src.insert(db_update)




# client = MongoClient("mongodb+srv://machinego:machinego123@mememachine-dopfr.gcp.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test

# db = client.get_database('ImageSource')
# src = db.source 



