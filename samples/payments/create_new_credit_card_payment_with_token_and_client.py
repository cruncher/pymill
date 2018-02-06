payment_service = paymill_context.get_payment_service()
payment_with_token_and_client = payment_service.create(
    token='098f6bcd4621d373cade4e832627b4f6',
    client_id='client_33baaf3ee3251b083420'
)
