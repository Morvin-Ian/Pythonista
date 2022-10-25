# Threads
import concurrent.futures
import time


def sleep_func():
	print('Sleeping for 2 Seconds...')
	time.sleep(2)
	return 'Done'

with concurrent.futures.ThreadPoolExecutor() as exec:
	results = [exec.submit(sleep_func) for _ in range(10)] # list comprehesions
	for f in concurrent.futures.as_completed(results):
		print(f.result())
