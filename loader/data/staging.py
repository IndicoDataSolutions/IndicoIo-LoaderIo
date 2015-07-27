"""
Script for Staging from template
"""
import time

from loader.data.base import get_test, TEXT_APIS, IMAGE_APIS, TEST_DURATION

DOMAIN = "staging.indico.domains"
APIS = TEXT_APIS + IMAGE_APIS
TESTS = [
    get_test(
        DOMAIN,
        api,
        time.strftime("%Y-%m-%d %H:%M:%S",
            time.gmtime(time.time() + 360 + TEST_DURATION * offset)
        )
    ) for offset, api in enumerate(APIS)
]


BATCH_TESTS = [
    get_test(
        DOMAIN,
        api,
        time.strftime("%Y-%m-%d %H:%M:%S",
            time.gmtime(
                time.time() + 360 + TEST_DURATION * len(APIS) + TEST_DURATION * offset
            )
        ),
        batch = True
    ) for offset, api in enumerate(APIS)
]
