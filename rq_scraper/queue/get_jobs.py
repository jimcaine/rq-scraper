import pandas as pd
from .get_schedulers import get_schedulers
from .get_queues import get_queues

def __jobs_to_df(jobs):

    scheduled_jobs = jobs['scheduler']
    df_scheduled = pd.DataFrame(
        zip(scheduled_jobs, ['scheduled']*len(scheduled_jobs)),
        columns=['job_id', 'status'])

    queued_jobs = jobs['queue']
    df_queued = pd.DataFrame(
        zip(queued_jobs, ['queued']*len(queued_jobs)),
        columns=['job_id', 'status'])

    df = pd.concat([df_scheduled, df_queued])
    return df

def get_jobs():

    jobs = {
        'scheduler': [],
        'queue': [],
    }

    schedulers = get_schedulers()
    for _, scheduler in schedulers.items():
        jobs['scheduler'] += scheduler.get_jobs()

    queues = get_queues()
    for _, queue in queues.items():
        jobs['queue'] += queue.get_jobs()

    return __jobs_to_df(jobs)
