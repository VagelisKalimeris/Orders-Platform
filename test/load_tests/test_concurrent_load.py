

def test_concurrent_orders_retrieval_and_produce_stats(load_test_client):
    load_test_client.do_concurrent_users_get_calls(100, '/orders')
