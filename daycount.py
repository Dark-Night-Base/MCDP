# -*- coding: utf-8 -*-
import copy
import datetime
import re
from utils import config, constant

startday = None

def on_load(server, old_module):
    global startday
    pluginconfig = config.Config(server, constant.CONFIG_FILE)
    pluginconfig.read_config()
    startday = datetime.datetime.strptime(str(pluginconfig['startday']), '%Y-%m-%d')


def on_info(server, info):
  global startday
  if info.content.startswith('!!day'):
    server.reply(info, '今天是这个服务器开服的第' + getday() + '天')


def getday():
  now = datetime.datetime.now()
  output = now - startday
  return str(output.days)
