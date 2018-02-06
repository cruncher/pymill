subscription_service = paymill_context.get_subscription_service()
subscription_with_an_offer = subscription_service.create_with_offer_id(
    payment_id='pay_3af44644dd6d25c820a9',
    offer_id='offer_bb33ea77b942f570997b'
)
