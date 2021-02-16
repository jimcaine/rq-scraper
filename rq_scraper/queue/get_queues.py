from .get_schedulers import get_schedulers
from rq_scraper.dataio.rqio import get_rq_conn

def get_queues():
    """

    """

    # create connection to redis server
    rq_conn = get_rq_conn()

    # get dictionary of all schedulers
    schedulers = get_schedulers()
    queues = {k:v.queue_class(k, connection=rq_conn)
              for k,v in schedulers.items()}
    return queues
