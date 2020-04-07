# -*- coding: utf-8 -*-
import copy
import datetime
import re
from utils import config, constant

startday = None

def on_load(server, old_module):
    global startday
    pluginconfig = config.Config(constant.CONFIG_FILE)
    pluginconfig.read_config()
    startday = pluginconfig['startday']


def on_info(server, info):
  global startday
  if info.content.startswith('!!day set'):
    try:
      newstartstr = re.match(r'!!day set (\S*)', info.content).groups()[0]
      newstartday = datetime.datetime.strptime(newstartstr, '%Y-%m-%d')
    except:
      server.reply(info, '§cPlease enter start day as yyyy-mm-dd')
    else:
      startday = newstartday
      server.reply(info, '§7Start day set as %s' % newstartstr)
  elif info.content.startwith('!!day'):
    server.reply(info, '今天是这个服务器开服的第' + getday() + '天')


def getday():
  now = datetime.datetime.now()
  output = now - startday
  return str(output.days)
