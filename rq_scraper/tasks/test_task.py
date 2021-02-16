import time
from rq_scraper.dataio.mongoio import insert_page

def test_task():
    insert_page({'ts': int(time.time())})
