from .get_mongo_client import mongo_client

def upsert_queue(queue_name, queue_object):
    cursor = mongo_client.db.queues.replace_one(
        filter={'_id': queue_name},
        replacement=queue_object,
        upsert=True)
    return cursor

def read_queue(queue_name):
    cursor = mongo_client.db.queues.find({'_id': queue_name})
    queue = list(cursor)[0]
    return queue

def read_queues():
    cursor = mongo_client.db.queues.find({})
    queues = [doc['_id'] for doc in list(cursor)]
    return queues

def delete_queue(queue_name):
    cursor = mongo_client.db.queues.delete_one({'_id': queue_name})
    return cursor
