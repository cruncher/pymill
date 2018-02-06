transaction_service = paymill_context.get_transaction_service()
transaction_with_payment = transaction_service.create_with_payment_id(
    payment_id='pay_3af44644dd6d25c820a9',
    amount=4200,
    currency='EUR',
    description='Test Transaction'
)
