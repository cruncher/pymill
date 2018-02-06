refund_service = paymill_context.get_refund_service()
refund_transaction = refund_service.refund_transaction(
    transaction_id='tran_ca3e7d41fb16d0157a99',
    amount=4200
)
