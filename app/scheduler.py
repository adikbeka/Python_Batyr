from rq_scheduler import Scheduler
from datetime import datetime

from dependencies import get_redis
from tasks import hello_world

RUN_INTERVAL = 30

def create_scheduler():
    redis = get_redis()
    scheduler = Scheduler(connection=redis)
    scheduler.schedule(scheduled_time=datetime.utcnow(),
                       func=hello_world,
                       interval=RUN_INTERVAL)