webhook_service = paymill_context.get_webhook_service()
url_webhook = webhook_service.create_url(
    url='<your-webhook-url>',
    event_types=['transaction.succeeded', 'transaction.failed'],
    active=True
)
