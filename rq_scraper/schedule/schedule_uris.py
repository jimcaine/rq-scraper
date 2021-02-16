from datetime import datetime, timedelta
import pandas as pd
from rq_scraper.dataio.mongoio import read_queue
from rq_scraper.queue import get_schedulers
from rq_scraper.tasks import test_task

def schedule_uris(uris, queue_name):
    """
    Schedules a list of uris to be scraped.

    Parameters
    ----------
    uris : list[str]
        List of URIs to be scraped.

    cfg : dict
        URI scraping configuration.
    """

    # create dataframe to store data
    df = pd.DataFrame(uris, columns=['uri'])

    # append rotating queue
    schedulers = get_schedulers()
    schedulers = schedulers.values()
    schedulers = [item for sublist in
        [schedulers for _ in range(int(df.shape[0]/len(schedulers))+1)]
        for item in sublist]
    schedulers = schedulers[0:df.shape[0]]
    df['scheduler'] = schedulers
    df['queue_name'] = df.scheduler.apply(lambda s: s.queue_name)

    # assign schedule time to each record
    queue = read_queue(queue_name)
    schedule_interval = queue['schedule_interval']
    if schedule_interval > 0:
        df['queue_rank'] = df.groupby(['queue_name']).cumcount().values
        df['schedule_time'] = df.queue_rank.apply(lambda i:
            datetime.utcnow() + timedelta(seconds=schedule_interval*i))
        df.drop(['queue_rank'], axis=1, inplace=True)
    else:
        df['schedule_time'] = [datetime.utcnow()] * df.shape[0]

    # schedule each row
    for _, row in df.iterrows():
        scheduler = row.scheduler
        scheduler.enqueue_at(
            row.schedule_time,
            func=test_task,
        )

    # return df
    return df
