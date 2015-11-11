import celery
import celery.schedules

cluster = celery.Celery(
    include=[
        'tasks'
    ]
)

cluster.conf.update(**{
    'BROKER_URL': 'pyamqp://cluster_test:test@localhost:5672',  # default RabbitMQ broker
    'CELERY_RESULT_BACKEND': 'amqp://cluster_test:test@localhost:5672',  # default RabbitMQ backend
    'CELERYBEAT_SCHEDULE': {
        'go-cluster': {
            'task': 'tasks.start_cluster',
            'schedule': celery.schedules.crontab(hour=22, minute=35),
            'args': [5000]
        }
    }
})

cluster.log.setup()

# logger = cluster.log.get_default_logger()

if __name__ == '__main__':
    cluster.start()