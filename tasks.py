import celery_cluster

import celery
import celery.utils.log

import logging
import time


logger = celery.utils.log.get_task_logger(__name__)
logger.level = logging.INFO


@celery_cluster.cluster.task()
def do_process(num):
    logger.info(num)
    time.sleep(.2)
    return num


@celery_cluster.cluster.task()
def start_cluster(n):

    logger.info(n)

    tasks = []

    for num in range(n):
        tasks.append(do_process.si(num))

    celery.chord(
        tasks,
        finish.s()
    )()


@celery_cluster.cluster.task()
def finish(results):

    for result in results:
        logger.info('result: {}'.format(result))
