subscription_service = paymill_context.get_subscription_service()
subscription_without_offer.name = 'Updated Subscription'
subscription_service.update(subscription_without_offer)
