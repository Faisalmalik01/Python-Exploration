# Implement an exponentaial backoff algorithm that doubles the wait time between retries, starting from 1 second, but stops after the 5th retries.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1}: Waiting for {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
