# -*- coding: utf-8 -*-
from mcdreforged.api.all import *
from mcdreforged.api.command import *



PLUGIN_METADATA = {
	'id': 'carpet_log',
	'version': '1.0.0',
	'name': 'log',
	'author': [
		'Tcilay'
    ],
    'dependencies' :  {
	    'mcdreforged': '>=1.0.0'
    }   
}

help_msg = '''
------ {0} {1} ------
carpet log 显示
§e!!{0} §3显示帮助信息
§e!!{0} clear  §3清空log
§e!!{0} tps §3 在tab界面显示服务器卡顿情况TPS,MSPT
§e!!{0} mobcaps  §3显示刷怪上限信息
§e!!{0} mobcapsLocal  §3显示局部刷怪上限信息
'''.format("log", "1.0.0")



def player_help(source: CommandSource):
    source.reply(help_msg)
    


def log_action(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    
    server = source.get_server()
    if dic.get("action") == "clear":
        server.execute('execute as {0} run log clear'.format(source.player))
        source.reply("§e清空log成功")
    if dic.get("action") == "tps":
        server.execute('execute as {0} run log tps'.format(source.player))
        source.reply("§e显示tps成功")
    if dic.get("action") == "mobcaps":
        server.execute('execute as {0} run log mobcaps'.format(source.player))
        source.reply("§e显示刷怪上限信息成功")
    if dic.get("action") == "mobcapsLocal":
        server.execute('execute as {0} run log mobcapsLocal'.format(source.player))
        source.reply("§e显示局部刷怪上限信息成功")
        
def on_load(server, prev_module):
    

    server.register_help_message('!!log','显示服务器信息')

    builder = SimpleCommandBuilder()

    builder.command('!!log <action>', log_action)
    builder.command('!!log', player_help)
    builder.arg('action', Text)

    builder.register(server)


