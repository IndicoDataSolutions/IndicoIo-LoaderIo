"""
Main LoaderIO Script to create Load Tests
"""
import requests, json

from loader.data.base import LOADERIO_URL, LOADERIO_HEADERS

def create(domain):
    module = __import__("loader.data.staging", fromlist=["loader.data"])
    for test in module.TESTS + module.BATCH_TESTS:
        response = json.loads(requests.post(
            LOADERIO_URL,
            headers = LOADERIO_HEADERS,
            data = json.dumps(test)
        ).text)
        print response

def run(domain):
    import time
    tests = [test["test_id"] for test in
        json.loads(requests.get(LOADERIO_URL, headers = LOADERIO_HEADERS).text)
        if domain in test["name"]
    ]

    for test in tests:
        result = requests.put(
            LOADERIO_URL + "/%s/run" % test,
            headers = LOADERIO_HEADERS).text
        print result
        time.sleep(60)

if __name__ == "__main__":
    import sys
    create(sys.argv[1])
    run(sys.argv[1])
