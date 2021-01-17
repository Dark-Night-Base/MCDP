# -*- coding: utf-8 -*-
import time

help_msg = '''------ §aMCR 时钟插件帮助信息 §f------
§b!!time help §f- §c显示帮助消息
§b!!time ct §f- §c显示当前时间
§b!!time timer [秒] §f- §c开启倒计时
§b!!time stopwatch start §f- §c开启秒表
§b!!time stopwatch stop §f- §c停止秒表
--------------------------------'''

no_input = '''------ §a温馨提示 §f------
§c未知指令 请输入 !!time help 获取帮助
--------------------------------'''

stop_T = False


def on_info(server, info):
    if info.is_player == 1:
        if info.content.startswith('!!time'):
            args = info.content.split(' ')
            if len(args) == 1:
                for line in help_msg.splitlines():
                    server.tell(info.player, line)
            elif args[1] == 'help':
                for line in help_msg.splitlines():
                    server.tell(info.player, line)
            elif args[1] == 'ct':
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
                int_current_time = int(time.strftime("%H", t))
                if int_current_time in range(6, 12):
                    server.tell(info.player, "------ §a当前时间 §f------")
                    server.tell(info.player, "§b 早上好")
                    server.tell(info.player, "§b 现在时间是: " + current_time)
                    server.tell(info.player, "--------------------------------")
                elif int_current_time in range(12, 19):
                    server.tell(info.player, "------ §a当前时间 §f------")
                    server.tell(info.player, "§b 下午好")
                    server.tell(info.player, "§b 现在时间是: " + current_time)
                    server.tell(info.player, "--------------------------------")
                elif int_current_time in range(19, 24):
                    server.tell(info.player, "------ §a当前时间 §f------")
                    server.tell(info.player, "§b 晚上好")
                    server.tell(info.player, "§b 现在时间是: " + current_time)
                    server.tell(info.player, "--------------------------------")
                elif int_current_time in range(0, 6):
                    server.tell(info.player, "------ §a当前时间 §f------")
                    server.tell(info.player, "§b 晚上好")
                    server.tell(info.player, "§b 现在时间是: " + current_time)
                    server.tell(info.player, "--------------------------------")
                else:
                    server.tell(info.player, "------ §a当前时间 §f------")
                    server.tell(info.player, "§b 现在时间是: " + current_time)
                    server.tell(info.player, "--------------------------------")
            elif args[1] == 'timer':
                second = int(args[2])
                count = 0
                while count < second:
                    count_now = second - count
                    if count_now >= 30:
                        server.tell(info.player, "倒计时还剩: " + "§a" + str(count_now))
                        time.sleep(1)
                        count += 1
                    elif 30 > count_now > 10:
                        server.tell(info.player, "倒计时还剩: " + "§e" + str(count_now))
                        time.sleep(1)
                        count += 1
                    else:
                        server.tell(info.player, "倒计时还剩: " + "§c" + str(count_now))
                        time.sleep(1)
                        count += 1
                server.tell(info.player, "时间到!")
                server.execute(
                    'execute at ' + info.player + ' run playsound minecraft:block.bell.use player ' + info.player)
                server.execute(
                    'execute at ' + info.player + ' run playsound minecraft:block.bell.use player ' + info.player)
                server.execute(
                    'execute at ' + info.player + ' run playsound minecraft:block.bell.use player ' + info.player)
            elif args[1] == 'stopwatch':
                status = args[2]
                if status == 'start':
                    start(server, info)
                elif status == 'stop':
                    stop(server, info)
            else:
                for line in no_input.splitlines():
                    server.tell(info.player, line)


def on_load(server, old):
    server.add_help_message('!!time', '时钟系统帮助')


def start(server, info):
    global stop_T
    stop_T = True
    start_time = time.time()
    server.tell(info.player, "§b秒表开启")
    while stop_T:
        r = round(time.time() - start_time, 0)
        server.tell(info.player, "§b计时: " + str(r) + " 秒")
        time.sleep(1)


def stop(server, info):
    global stop_T
    if stop_T:
        stop_T = False
        server.tell(info.player, "§b秒表已停止")
    else:
        server.tell(info.player, "§b秒表未开启")
