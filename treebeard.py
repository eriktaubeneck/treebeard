# -*- coding: utf-8 -*-

import re

from slackbot.bot import Bot, PluginsManager
from slackbot.dispatcher import MessageDispatcher
from slackbot.utils import to_utf8
from six import iteritems


class TreebeardDispatcher(MessageDispatcher):
    def _default_reply(self, msg):
        default_reply = [
            u"That doesn't make sense to me. But, then again, you are very small. \n "
            u'You can ask me one of the following questions:\n',
        ]
        default_reply += [u'    • `{0}` {1}'.format(p.pattern, v.__doc__ or "")
                          for p, v in iteritems(self._plugins.commands['respond_to'])]

        self._client.rtm_send_message(
            msg['channel'],
            '\n'.join(to_utf8(default_reply))
        )


class TreebeardPluginsManager(PluginsManager):
    def init_plugins(self):
        super(TreebeardPluginsManager, self).init_plugins()
        for command, func in iteritems(self.commands['respond_to']):
            new_command = re.compile('gcbot {}'.format(command.pattern), command.flags)
            self.commands['listen_to'][new_command] = func
            new_command = re.compile('treebeard {}'.format(command.pattern), command.flags)
            self.commands['listen_to'][new_command] = func



class TreebeardBot(Bot):
    def __init__(self):
        super(TreebeardBot, self).__init__()
        self._plugins = TreebeardPluginsManager()
        self._dispatcher = TreebeardDispatcher(self._client, self._plugins)
