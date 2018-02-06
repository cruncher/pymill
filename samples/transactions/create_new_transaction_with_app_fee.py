transaction_service = paymill_context.get_transaction_service()
transaction_with_token = transaction_service.create_with_token(
    token='098f6bcd4621d373cade4e832627b4f6',
    amount=4200, currency='EUR',
    description='Test Transaction',
    fee_amount=4200,
    fee_payment_id='pay_3af44644dd6d25c820a8',
    fee_currency='EUR'
)
