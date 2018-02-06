preauthorization_service = paymill_context.get_preauthorization_service()
preauthorization_with_token = preauthorization_service.create_with_token(
    token='098f6bcd4621d373cade4e832627b4f6',
    amount=4200,
    currency='EUR',
    description='description example'
)
