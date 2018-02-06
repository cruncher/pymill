# pause
subscription_service = paymill_context.get_subscription_service()
subscription_service.pause(subscription_without_offer)
# unpause
subscription_service = paymill_context.get_subscription_service()
subscription_service.unpause(subscription_without_offer)
