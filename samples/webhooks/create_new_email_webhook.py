webhook_service = paymill_context.get_webhook_service()
email_webhook = webhook_service.create_email(
    email='lovely-webhook@example.com',
    event_types=['transaction.succeeded', 'transaction.failed'],
    active=True
)
