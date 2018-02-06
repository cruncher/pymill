payment_service = paymill_context.get_payment_service()
payment_with_token_and_client = payment_service.create(
    token='12a46bcd462sd3r3care4e8336ssb4f5',
    client_id='client_33baaf3ee3251b083420'
)
