# -*- coding: utf-8 -*-

import requests
from slackbot import settings


def image_search(search_term):
    params = {
        'q': search_term,
        'num': 1,
        'start': 1,
        'imgSize': 'medium',
        'fileType': 'jpg',
        'safe': 'medium',
        'key': settings.GOOGLE_API_KEY,
        'cx': settings.GOOGLE_CX,
    }
    r = requests.get(
        'https://www.googleapis.com/customsearch/v1',
        params=params
    )
    j = r.json()
    results = j['items']
    if not results:
        return
    result = results[0]
    image_loc = result['pagemap']['cse_image'][0]['src']
    return image_loc
