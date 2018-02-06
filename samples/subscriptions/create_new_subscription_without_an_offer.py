subscription_service = paymill_context.get_subscription_service()
subscription_without_offer = subscription_service.create_with_amount(
    payment_id='pay_5e078197cde8a39e4908f8aa',
    amount=3OOO,
    currency='EUR',
    interval='1 WEEK,MONDAY'
)
