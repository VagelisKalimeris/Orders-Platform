from statistics import stdev
from time import time
from threading import Lock, Thread


from test.nano_test_framework.http_client import OrdersTestClient


class LoadTestClient(OrdersTestClient):
    def __init__(self):
        super().__init__()

    def calculate_get_resp_time(self, path: str, times_list: list, lock: Lock):
        start_time = time()
        # Make call and validate status code
        self.get(path)
        end_time = time()

        response_time = end_time - start_time

        with lock:
            times_list.append(response_time)

    def do_concurrent_users_get_calls(self, users, path):
        response_times, threads = [], []
        lock = Lock()

        # Start user threads
        for _ in range(users):
            thread = Thread(target=self.calculate_get_resp_time(path, response_times, lock))
            threads.append(thread)
            thread.start()

        # Wait for user threads to complete
        for thread in threads:
            thread.join()

        # Calculate average response time
        avg_response_time = sum(response_times) / users
        # Calculate the standard deviation
        standard_deviation = stdev(response_times)

        print(f"\n\nAverage '{path}' Response Time for {users} users: {avg_response_time:.3f} seconds.")
        print(f"Standard '{path}' Deviation for {users} users: {standard_deviation:.3f} seconds.\n")
