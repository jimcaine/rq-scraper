from pymongo import MongoClient
from . import __env as env

def get_mongo_client():
    """
    Creates and returns a connection to Redis server.
    """

    client = MongoClient(
        host=env.MONGO_HOST,
        port=int(env.MONGO_PORT),
    )

    return client

mongo_client = get_mongo_client()
