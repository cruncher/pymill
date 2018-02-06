subscription_service = paymill_context.get_subscription_service()
subscription_with_an_offer.offer_id='offer_40237e20a7d5a231d99b'
subscription_service.update_with_offer_id(
    subscription_with_an_offer,
    offer_change_type=2
)
