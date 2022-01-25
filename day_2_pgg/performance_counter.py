import time

start = time.perf_counter()
time.sleep(1)
stop = time.perf_counter()
print(f'Duration: {stop-start} s')