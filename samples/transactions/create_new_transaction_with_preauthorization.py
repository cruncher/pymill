transaction_service = paymill_context.get_transaction_service()
transaction_with_preauthorization = transaction_service.create_with_preauthorization_id(
    preauthorization_id='preauth_ec54f67e52e92051bd65',
    amount=4200, currency='EUR',
    description='Test Transaction'
)
