# -*- coding: utf-8 -*-
import minecraft_data_api as api
from mcdreforged.api.all import *
from mcdreforged.api.command import *



PLUGIN_METADATA = {
	'id': 'player_bot',
	'version': '1.0.1',
	'name': 'player_bot',
	'author': [
		'Tcilay'
    ],
    'dependencies' :  {
        'minecraft_data_api': '*'
    }   
}


bot_Prefix = "bot_"
help_msg = '''
------ {1} {2} ------
一个管理假人的MCDR§a插件
§3作者：Tcilay
§e!!{0} §3显示帮助信息
§e!!{0} <bot> spawn  §3召唤假人
§e!!{0} <bot> tp  §3召唤存在假人到你的位置
§e!!{0} <bot> kill  §3下线假人
§e!!{0} <bot> swapHands §3假人交换主副手物品
§e!!{0} <bot> drop [<options>] §3假人丢弃物品
§e!!{0} <bot> use [<options>]§3假人使用物品
§e!!{0} <bot> dropStack [<options>] §3假人丢弃一组物品
§e!!{0} <bot> jump [<options>] §3假人跳跃
§e!!{0} <bot> attack [<options>] §3假人攻击
§e!!{0} <bot> move [<options>] §3假人移动
§e!!{0} <bot> look [<options>] §3假人看向
'''.format("player", "player", "1.0.1")



dim_convert = {
    0 : 'minecraft:overworld',
    -1: 'minecraft:the_nether',
    1 : 'minecraft:the_end'
}

def get_dimension_translation_text(dim):
    return dim_convert[dim]

def player_help(source: CommandSource):
    source.reply(help_msg)
    


@new_thread(PLUGIN_METADATA['name'])
def player_action(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    

    server = source.get_server()
    action = str(dic.get("action"))
    player = source.player
    name = bot_Prefix +dic.get("bot")
    if action == "spawn":
        coord = api.get_player_coordinate(player)
        dim = api.get_player_dimension(player)
        dim_text = get_dimension_translation_text(dim)
        server.execute('execute in {0} run player {1} spawn at {2} {3} {4}'.format(dim_text, name, coord.x, coord.y, coord.z))
    elif action == "tp":
        server.execute('tp ' + name + " " + player)
    elif action == "kill":
        server.execute('player ' + name + " kill")
    elif action == "stop":
        server.execute('player ' + name + " stop")
    elif action == "swapHands":
        server.execute('player ' + name + " swapHands")
    else:
        source.reply("§c§l错误的指令")


def player_action_1(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    
    server = source.get_server()
    action = str(dic.get("action"))
    name = bot_Prefix +dic.get("bot")
    other = dic.get("other")
    if action == "use":
        server.execute('player ' + name + ' use ' + other)
    elif action == "attack":
        server.execute('player ' + name + ' attack ' + other)
    elif action == "jump":
        server.execute('player ' + name + ' jump ' + other)
    elif action == "move":
        server.execute('player ' + name + ' move ' + other)
    elif action == "look":
        server.execute('player ' + name + ' look ' + other)
    elif action == "drop":
        server.execute('player ' + name + ' drop ' + other)
    elif action == "dropStack":
        server.execute("player " + name + " dropStack " + other)
    else:
        source.reply("§c§l错误的指令")


def on_load(server, prev_module):
    

    server.register_help_message('!!player', '假人管理')

    builder = SimpleCommandBuilder()


    builder.command('!!player', player_help)
    builder.command('!!player <bot> <action>', player_action)
    builder.command('!!player <bot> <action> <other>', player_action_1)

    builder.arg('bot', Text)
    builder.arg('action', Text)
    builder.arg('other', Text)

    builder.register(server)
