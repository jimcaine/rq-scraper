from redis import Redis
from rq import Queue
from rq_scheduler import Scheduler
from rq_scraper.dataio.mongoio import read_queues
from rq_scraper.dataio.rqio import get_rq_conn

def get_schedulers():
    """
    """

    # create connection to redis server
    rq_conn = get_rq_conn()

    # get queue_names from app data store
    queue_names = read_queues()

    # build schedulers object
    schedulers = {}
    for queue_name in queue_names:
        schedulers[queue_name] = Scheduler(queue_name, connection=rq_conn)

    # return dictionary of schedulers
    return schedulers
