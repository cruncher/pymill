client_service = paymill_context.get_client_service()
client.email = 'lovely-client-updated-email@example.com'
client_service.update(client)
