# -*- coding: utf-8 -*-

import logging
import sys

from treebeard import TreebeardBot
from slackbot import settings


def main():
    kw = {
        'format': '[%(asctime)s] %(message)s',
        'datefmt': '%m/%d/%Y %H:%M:%S',
        'level': logging.DEBUG if settings.DEBUG else logging.INFO,
        'stream': sys.stdout,
    }
    logging.basicConfig(**kw)
    logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)

    bot = TreebeardBot()
    bot.run()


if __name__ == '__main__':
    main()
