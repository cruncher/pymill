preauthorization_service = paymill_context.get_preauthorization_service()
preauthorization_with_payment = preauthorization_service.create_with_payment_id(
    payment_id ='pay_3af44644dd6d25c820a9',
    amount=4200,
    currency='EUR',
    description='description example'
)
