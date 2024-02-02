# -*- coding: utf-8 -*-


from mcdreforged.api.all import *


import database as db
import func as f


db = db.Database() 


def step_add(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
        
    player = f.get_player_pos(source.player)
    server = source.get_server()
    type=dic.get('type')
    if type == '' or type == None or f.trans_type(dic.get('type')) == '-1' :
        source.reply('你的位置：'+player.text(),
                     '§c请指定类型:',
                     f.trans_list()
                     )
        return
    if type == '0' & dic.get('msg') == None:
        source.reply('§c类型为其他，请指定备注！')
        return
    
    db.add(player.name,player.dim_num, player.x, player.y, player.z, dic.get('type'), dic.get('msg'))


def step(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    player = f.get_player_pos(source.player)
    server = source.get_server()
    data=db.search(player.dim_num, player.x, player.y, player.z,)
    for i in data:
        step += "§a id:"+i['id']+"§c"+f.trans_type(i['type'])+"@"+i['msg']+"  §r["+i['x']+","+ i['y']+","+i['z']+"\n"
    source.reply(step)

def step_search(source: CommandSource, dic: dict):
    if source.is_player == False:
        source.reply('§c请在游戏中执行该命令')
        return
    player = f.get_player_pos(source.player)
    server = source.get_server()
    type=dic.get('type')
    if type == '' or type == None or f.trans_type(dic.get('type')) == '-1':
        source.reply('§c未知的类型:',
                     f.trans_list()
                     )
    data=db.search_type(type)
    
    for i in data:
        step += "§a id:"+i['id']+"§c"+f.trans_type(i['type'])+"@"+i['msg']+"  §r["+i['x']+","+ i['y']+","+i['z']+"\n"
        
        # Search data pagination
        if dic.get("page") == None:
            page = 1
        else:
            page = int(dic.get("page"))
        
        total_steps = len(data)
        steps_per_page = 10
        start_index = (page-1) * steps_per_page
        end_index = start_index + steps_per_page
        
        if end_index > total_steps:
            end_index = total_steps
        
        for j in range(start_index, end_index):
            step += "§a 第" + str(page) + "页\n"


def on_load(server, prev_module):
    

    server.register_help_message('!!step help', '足迹帮助')
    server.register_help_message('!!loc help', '坐标帮助')

    builder = SimpleCommandBuilder()


    builder.command('!!loc', loc)
    builder.command('!!loc help', loc_help)
    builder.command('!!step', step)
    builder.command('!!step help', step_help)
    builder.command('!!step add', step_add)
    builder.command('!!step add <type>', step_add)
    builder.command('!!step add <type> <msg>', step_add)
    builder.command('!!step search <type>', step_search)
    builder.command('!!step search <type> <page>', step_search)

    builder.arg('type', Text)
    builder.arg('msg', Text)
    builder.arg('page', Text)


    builder.register(server)

