import celery

cluster = celery.Celery(
    include=[
        'tasks'
    ]
)

cluster.conf.update(**{
    'BROKER_URL': 'pyamqp://cluster_test:test@localhost:5672',  # default RabbitMQ broker
    'CELERY_RESULT_BACKEND': 'amqp://cluster_test:test@localhost:5672',  # default RabbitMQ backend
    # 'CELERY_REDIRECT_STDOUTS_LEVEL': DEBUG
})

cluster.log.setup()

# logger = cluster.log.get_default_logger()

if __name__ == '__main__':
    cluster.start()