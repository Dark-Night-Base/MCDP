# -*- coding: utf-8 -*-
import os
import shutil
import time
from typing import List, Tuple

from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'region_file_updater',
    'version': '1.3.0',
    'name': 'Region file Updater',
    'description': 'A MCDR plugin to help you update region files in game',
    'author': 'Fallen_Breath',
    'link': 'https://github.com/TISUnion/RegionFileUpdater',
    'dependencies': {
            'minecraft_data_api': '*',
    }
}

SourceWorldPath = './qb_multi/slot1/world/'
DestinationWorldPath = './server/world/'
Prefix = '!!region'
PluginName = PLUGIN_METADATA['name']
LogFilePath = os.path.join('logs', '{}.log'.format(PluginName))
DimensionRegionFolder = {
    -1: 'DIM-1/region/',
    0: 'region/',
    1: 'DIM1/region/'
}
HelpMessage = '''
------MCDR {1} v{2}------
一个更新本服区域文件至生存服!!qb存档区域文件的插件
§a【指令说明】§r
§7{0} §r显示帮助信息
§7{0} add §r添加玩家所在位置的区域文件
§7{0} add §6[x] [z] [d] §r添加指定的区域文件
§7{0} del §r删除玩家所在位置的区域文件
§7{0} del §6[d] [x] [z] [d] §r删除指定的区域文件
§7{0} del-all §r删除所有区域文件
§7{0} list §r列出待更新的区域文件
§7{0} history §r输出上一次update的结果
§7{0} update §r更新列表中的区域文件，这将重启服务器
§a【参数说明】§r
§6[x] [z]§r: 区域文件坐标，如r.-3.1.mca的区域文件坐标为x=-3 z=1
§6[d]§r: 维度序号，主世界为0，下界为-1，末地为1
'''.strip().format(Prefix, PLUGIN_METADATA['name'], PLUGIN_METADATA['version'])

regionList = []  # type: List[Region]
historyList = []  # type: List[Tuple[Region, bool]]


class Region:
    def __init__(self, x: int, z: int, dim: int):
        self.x = x
        self.z = z
        self.dim = dim

    def to_file_name(self):
        return 'r.{}.{}.mca'.format(self.x, self.z)

    def to_file_path(self):
        return os.path.join(DimensionRegionFolder[self.dim], self.to_file_name())

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.x == other.x and self.z == other.z and self.dim == other.dim

    def __repr__(self):
        return 'Region[x={}, z={}, dim={}]'.format(self.x, self.z, self.dim)


def print_log(msg: str):
    with open(LogFilePath, 'a') as logfile:
        logfile.write(time.strftime('%Y-%m-%d %H:%M:%S',
                                    time.localtime(time.time())) + ': ' + msg + '\n')


def add_region(source: CommandSource, region: Region):
    if region in regionList:
        source.reply('列表中已存在该区域文件')
    else:
        regionList.append(region)
        source.reply('区域文件§6{}§r已添加'.format(region))


def delete_region(source: CommandSource, region: Region):
    if region not in regionList:
        source.reply('列表中不存在该区域文件')
    else:
        regionList.remove(region)
        source.reply('区域文件§6{}§r已删除'.format(region))


def clean_region_list(source):
    regionList.clear()
    source.reply('区域文件列表已清空')


def get_region_from_source(source: PlayerCommandSource) -> Region:
    api = source.get_server().get_plugin_instance('minecraft_data_api')
    coord = api.get_player_coordinate(source.player)
    dim = api.get_player_dimension(source.player)
    return Region(int(coord.x) // 512, int(coord.z) // 512, dim)


@new_thread(PLUGIN_METADATA['name'])
def add_region_from_player(source: CommandSource):
    if isinstance(source, PlayerCommandSource):
        add_region(source, get_region_from_source(source))
    else:
        source.reply('该指令仅支持玩家执行')


@new_thread(PLUGIN_METADATA['name'])
def delete_region_from_player(source: CommandSource):
    if isinstance(source, PlayerCommandSource):
        delete_region(source, get_region_from_source(source))
    else:
        source.reply('该指令仅支持玩家执行')


def show_region_list(source: CommandSource):
    source.reply('更新列表中共有{}个待更新的区域文件'.format(len(regionList)))
    for region in regionList:
        source.reply('- §6{}§r'.format(region))


def show_history(source: CommandSource):
    source.reply('上次尝试更新更新了{}个区域文件'.format(len(historyList)))
    msg = {False: '失败', True: '成功'}
    for region, flag in historyList:
        source.reply('§6{}§r: {}'.format(region, msg[flag]))


def region_update(source: CommandSource):
    show_region_list(source)
    countdown = 5
    source.reply('[{}]: {}秒后重启服务器更新列表中的区域文件'.format(
        PluginName, countdown), isBroadcast=True)
    for i in range(1, countdown):
        source.reply('[{}]: 还有{}秒'.format(
            PluginName, countdown - i), isBroadcast=True)
        time.sleep(1)

    source.get_server().stop()
    source.get_server().wait_for_start()

    source.get_server().logger.info('{} 更新了 {} 个区域文件：'.format(source, len(regionList)))
    historyList.clear()
    for region in regionList:
        source_dir = os.path.join(SourceWorldPath, region.to_file_path())
        destination = os.path.join(DestinationWorldPath, region.to_file_path())
        try:
            source.get_server().logger.info('- "{}" -> "{}"'.format(source_dir, destination))
            shutil.copyfile(source_dir, destination)
        except Exception as e:
            msg = '失败，错误信息：{}'.format(str(e))
            flag = False
        else:
            msg = '成功'
            flag = True
        historyList.append((region, flag))
        text = '  {}: {}'.format(region, msg)
        source.get_server().logger.info(text)
        print_log(text)

    regionList.clear()
    time.sleep(1)
    source.get_server().start()


def on_load(server: ServerInterface, old):
    server.register_help_message(Prefix, '从指定存档处更新region文件至本服')
    try:
        global historyList, regionList
        historyList = old.historyList
        regionList = old.regionList
    except AttributeError:
        pass

    def get_region_parm_node(callback):
        return Integer('x').then(Integer('z').then(Integer('dim').in_range(-1, 1).runs(callback)))

    server.register_command(
        Literal(Prefix).
        runs(lambda src: src.reply(HelpMessage)).
        on_error(UnknownCommand, lambda src: src.reply('参数错误！请输入§7{}§r以获取插件帮助'.format(Prefix)), handled=True).
        then(
            Literal('add').runs(add_region_from_player).
            then(get_region_parm_node(lambda src, ctx: add_region(
                src, Region(ctx['x'], ctx['z'], ctx['dim']))))
        ).
        then(
            Literal('del').runs(delete_region_from_player).
            then(get_region_parm_node(lambda src, ctx: delete_region(
                src, Region(ctx['x'], ctx['z'], ctx['dim']))))
        ).
        then(Literal('del-all').runs(clean_region_list)).
        then(Literal('list').runs(show_region_list)).
        then(Literal('history').runs(show_history)).
        then(Literal('update').runs(region_update))
    )
