from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'update-products-every-hour': {
        'task': 'economy.tasks.update_product_prices',
        'schedule': crontab(minute=0, hour='*/1'),
    },
    'update-inputs-every-hour': {
        'task': 'economy.tasks.update_input_prices',
        'schedule': crontab(minute=15, hour='*/1'),
    },
    'update-sales-every-hour': {
        'task': 'economy.tasks.update_sales_data',
        'schedule': crontab(minute=30, hour='*/1'),
    },
}