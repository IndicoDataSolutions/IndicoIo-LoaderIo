import os, json

LOADERIO_URL = "https://api.loader.io/v2/tests"
INDICO_API_KEY = os.environ.get("INDICO_API_KEY")
TEST_DURATION = 60
LOADERIO_HEADERS = {
    "loaderio-auth": os.environ.get("LOADERIO_API_KEY"),
    "Content-Type": "application/json"
}

API_DATA = {
    "headers": {
        "Content-Type": "application/json"
    },
    "request_type": "POST"
}

TEXT_API_DATA = dict(API_DATA, raw_post_body = json.dumps({
    "data": "Indico Data Solutions is the number one startup in Boston."
}))

IMAGE_API_DATA = dict(API_DATA, raw_post_body = json.dumps({
    "data": open(
        os.path.join(os.path.dirname(__file__), "image.txt"), 'rb'
    ).read()
}))

BATCH_TEXT_API_DATA = dict(API_DATA, raw_post_body = json.dumps({
    "data": ["Indico Data Solutions is the number one startup in Boston."]
}))

BATCH_IMAGE_API_DATA = dict(API_DATA, raw_post_body = json.dumps({
    "data": [open(
        os.path.join(os.path.dirname(__file__), "image.txt"), 'rb'
    ).read()]
}))

TEXT_APIS = ["sentiment", "sentimenthq", "keywords", "language", "namedentities", "texttags", "political"]
IMAGE_APIS = ["fer", "facialfeatures", "contentfiltering", "imagefeatures", "faciallocalization"]

def get_test(domain, api, schedule, batch = False):
    if api in TEXT_APIS:
        data = TEXT_API_DATA if not batch else BATCH_TEXT_API_DATA
    else:
        data = IMAGE_API_DATA if not batch else BATCH_IMAGE_API_DATA

    return {
        "test_type": "cycling",
        "initial": 50, # (connections)
        "total": 100, # (connections)
        "duration": TEST_DURATION, #(seconds)
        "error_threshold": 1,
        "next_run_at": schedule,
        "scheduled_at": schedule,
        "name": domain + "_" + api,
        "urls": [
            dict(data, url="https://%s/%s%s?key=%s" % (
                domain,
                api,
                "/batch" if batch else "",
                INDICO_API_KEY)
            ),
        ]
    }
