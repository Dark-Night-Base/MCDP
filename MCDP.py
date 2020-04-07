# -*- coding: utf-8 -*-

import os
import re
import shutil
from git import Repo

path = ''
repo = None
pluginlist = []


def copy_plugin(plugin: str) -> bool:
    "Copy a plugin and its folder. Return True if succeeded, otherwise return False"
    if not plugin.endswith('.py'):
        return False
    try:
        shutil.copy(path + plugin, path + '../')
    except:
        return False
    try:  # copy folder
        os.listdir(path + plugin[0:-3])
    except:
        return True
    else:
        try:  # remove existing folder in plugins/
            os.listdir(path + '../' + plugin[0:-3])
        except:
            pass
        else:
            shutil.rmtree(path + '../' + plugin[0:-3])
        shutil.copytree(path + plugin[0:-3], path + '../' + plugin[0:-3])
        return True


def remove_plugin(plugin: str) -> bool:
    "Remove a plugin and its folder. Return True if succeeded, otherwise return False"
    if not plugin.endswith('.py'):
        return False
    try:
        os.remove(path + '../' + plugin)
    except:
        return False
    try:  # remove folder
        shutil.rmtree(path + '../' + plugin[0:-3])
    except:
        pass
    return True


def on_load(server, old_module):
    global path, repo
    path = os.getcwd()  # MCDReforged/
    path += '/plugins/MCDP/'
    try:
        os.listdir(path)
    except:
        server.logger.info(
            'Directory \'plugins/MCDP\' not found, tring to create one...')
        os.mkdir(path)
    try:
        repo = Repo(path)
    except:
        server.logger.info(
            'Repo \'plugins/MCDP\' is bare, tring to clone one...')
        repo = Repo.clone_from('https://github.com/Dark-Night-Base/MCDP.git', path)
    else:
        repo.remote().pull()


def on_info(server, info):
    global path, repo, pluginlist
    if re.match('!!MCDP', info.content) != None:
        if info.content == '!!MCDP list':
            pluginlist = os.listdir(path)
            text = 'Listing...\n'
            for plugin in pluginlist:
                if plugin.endswith('.py'):
                    text += '§2' + plugin + '\n'
            server.reply(info, text)
        elif info.content.startswith('!!MCDP install'):
            try:
                plugin = re.match(r'!!MCDP install (\S*)',
                                  info.content).groups()[0]
            except:
                server.reply(info, '§cPlease specify plugin!')
            else:
                if plugin in pluginlist:
                    if copy_plugin(plugin):
                        text = '§aPlugin %s installed successfully!' % plugin
                        server.execute('!!MCDR reload plugin')
                    else:
                        text = '§cPlugin %s installed failed!\n' % plugin
                        text += '§cConsider add \'.py\' behind the name?'
                else:
                    text = '§cPlugin %s not found!' % plugin
                    text += '§cConsider add \'.py\' behind the name?'
                server.reply(info, text)
        elif info.content.startswith('!!MCDP remove'):
            try:
                plugin = re.match(r'!!MCDP remove (\S*)',
                                  info.content).groups()[0]
            except:
                server.reply(info, '§cPlease specify plugin!')
            else:
                if plugin in pluginlist:
                    if remove_plugin(plugin):
                        text = '§aPlugin %s removed successfully!' % plugin
                        server.execute('!!MCDR reload plugin')
                    else:
                        text = '§cPlugin %s removed failed!\n' % plugin
                        text += '§cConsider add \'.py\' behind the name?'
                else:
                    text = '§cPlugin %s not found!' % plugin
                    text += '§cConsider add \'.py\' behind the name?'
                server.reply(info, text)

        elif info.content == '!!MCDP update':
            fetchinfo = repo.remote().pull()[0]
            committime = fetchinfo.commit.authored_datetime.strftime(
                '%b %d %H:%M')
            server.reply(info, '§7Updated. Last commit at' +
                         committime + ':\n' + fetchinfo.commit.message)
        elif info.content == '!!MCDP upgrade':
            pluginlist = os.listdir(path)
            for plugin in pluginlist:
                if plugin.endswith('.py'):
                    copy_plugin(plugin)
            server.say('§7Plugins upgraded.')
            server.execute('!!MCDR reload plugin')
        else:
            text = '§7!!MCDP§r: Show this message\n'
            text += '§7!!MCDP list§r: List the plugins\n'
            text += '§7!!MCDP install [plugin]§r: Install or upgrade plugins\n'
            text += '§7!!MCDP remove [plugin]§r: Remove the plugins\n'
            text += '§7!!MCDP update§r: Update list of available plugins\n'
            text += '§7!!MCDP upgrade§r: Upgrade the plugins'
            server.reply(info, text)
