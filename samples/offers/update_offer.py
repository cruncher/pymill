offer_service = paymill_context.get_offer_service()
offer.name = 'Extended Special'
offer.interval = '1 MONTH'
offer.amount = 3333
offer.currency = 'USD'
offer.trial_period_days = '33'

offer_service.update(offer, true)
