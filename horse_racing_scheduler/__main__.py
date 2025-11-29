from apscheduler.schedulers.blocking import BlockingScheduler

import horse_racing_scheduler.utils as utils

L = utils.get_logger(__name__)


def hello():
    L.info("hello")


if __name__ == "__main__":
    scheduler = BlockingScheduler()

    scheduler.add_job(
        hello,
        "cron",
        misfire_grace_time=None,
        second="*/10",
    )

    try:
        L.info("Starting scheduler")
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
        L.info("Shutting down scheduler")
