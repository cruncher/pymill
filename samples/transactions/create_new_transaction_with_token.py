transaction_service = paymill_context.get_transaction_service()
transaction_with_token = transaction_service.create_with_token(
    token='098f6bcd4621d373cade4e832627b4f6',
    amount=4200,
    currency='EUR',
    description='Test Transaction'
)
