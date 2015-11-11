import celery

cluster = celery.Celery(
    include=[
        'tasks'
    ]
)

cluster.conf.update(**{
    'BROKER_URL': 'pyamqp://',  # default RabbitMQ broker
    'CELERY_RESULT_BACKEND': 'amqp://',  # default RabbitMQ backend
    # 'CELERY_REDIRECT_STDOUTS_LEVEL': DEBUG
})

cluster.log.setup()

# logger = cluster.log.get_default_logger()

if __name__ == '__main__':
    cluster.start()