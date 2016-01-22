# -*- coding: utf-8 -*-

import re
import logging

from slackbot.bot import respond_to
from utils.googleapi import image_search


logger = logging.getLogger(__name__)


@respond_to('image me (.*)', re.IGNORECASE)
def image_me(message, search_term):
    logger.debug('searching for {}'.format(search_term))
    image_loc = image_search(search_term)
    if not image_loc:
        message.reply('I have told your search to the Entmoot, '
                      'and we have agreed you are not Orcs. '
                      'However there were no images.')
    else:
        message.send(image_loc)
