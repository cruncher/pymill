transaction_service = paymill_context.get_transaction_service()
transaction_with_token.amount = 3200
transaction_with_token.currency = 'USD'
transaction_with_token.description = 'My updated transaction description'
transaction_service.update(transaction_with_token)
