from redis import Redis
from . import __env as env

def get_rq_conn():
    """
    Creates and returns a connection to Redis server.
    """

    connection = Redis(
        host=env.REDIS_SERVER_HOST,
        port=env.REDIS_SERVER_PORT,
    )

    return connection
