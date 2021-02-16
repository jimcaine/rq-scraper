from .get_mongo_client import mongo_client

def insert_page(page):
    cursor = mongo_client.db.pages.insert(page)
    return cursor
