# -*- coding: utf-8 -*-
import minecraft_data_api as api

from mcdreforged.api.all import *
from mcdreforged.api.command import *



PLUGIN_METADATA = {
	'id': 'player_box',
	'version': '1.0.0',
	'name': 'player_box',
	'author': [
		'Tcilay'
    ],
    'dependencies' :  {
        'minecraft_data_api': '*'
    }   
}


help_msg = '''
------ {1} {2} ------
一个随身箱子的MCDR§a插件
§3作者：Tcilay
§e!!{0} §3显示帮助信息
§e!!{0} spawn §3召唤你的箱子
§e!!{0} store §3存储你的箱子
§e!!{0} tp <player> §3将你的箱子送到别的玩家那

逻辑：先召唤再存储，先召唤再tp（别没存储就召唤，后果自负）
请确保你的身上没有运输矿车！
'''.format("box", "player_box", "1.0.0")

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
def box_spawn(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
        
    player = source.player
    server = source.get_server()

    coord = api.get_player_coordinate(player)
    dim = api.get_player_dimension(player)
    dim_text = get_dimension_translation_text(dim)

    print(coord.x, coord.y, coord.z,dim_text,dim)
    name = "\'\"{0}_chest\"\'".format(player)
    nbt = "{CustomName:"+name+",Tags:['box_"+player+"']}"
    
    server.execute("data modify storage player:box {0} set from entity @e[tag=box_{0},limit=1]".format(player))
    server.execute("data remove entity @e[tag=box_{0},limit=1] Items".format(player))
    server.execute("kill @e[name={0}_chest]".format(player))
    server.execute("execute in {1} run summon minecraft:chest_minecart {2} {3} {4} {5}".format(player,dim_text,coord.x,coord.y,coord.z,nbt))
    server.execute("data modify entity @e[tag=box_{0},limit=1] Items set from storage player:box {0}.Items".format(player))
    server.execute("data remove storage player:box {0}".format(player))
    server.execute("clear {0} minecraft:chest_minecart".format(player))


def box_storge(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    player = source.player
    server = source.get_server()
    server.execute("data modify storage player:box {0} set from entity @e[tag=box_{0},limit=1]".format(player))
    server.execute("data remove entity @e[tag=box_{0},limit=1] Items".format(player))
    server.execute("kill @e[tag=box_{0}]".format(player))

def box_tp(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    player = source.player
    server = source.get_server()
    player_name = dic.get("player")
    server.execute("tp @e[tag=box_{0}] {1}".format(player,player_name))

def on_load(server, prev_module):
    

    server.register_help_message('!!box', '随身箱子')

    builder = SimpleCommandBuilder()


    builder.command('!!box', player_help)
    builder.command('!!box spawn', box_spawn)
    builder.command('!!box store', box_storge)
    builder.command('!!box tp <player>', box_tp)

    builder.arg('player', Text)


    builder.register(server)

