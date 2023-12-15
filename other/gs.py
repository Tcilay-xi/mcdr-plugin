# -*- coding: utf-8 -*-
from mcdreforged.api.all import *
from mcdreforged.api.command import *



PLUGIN_METADATA = {
	'id': 'gs',
	'version': '1.0.0',
	'name': 'gs',
	'author': [
		'Tcilay'
    ],
    'dependencies' :  {
	    'mcdreforged': '>=1.0.0'
    }   
}


def get_op(source: CommandSource, dic: dict):
    server = source.get_server()
    server.say('<'+source.player+'> 我是原P！')
    server.say('<'+source.player+'> 我是黑塔的狗，快来测我！')
    #本人表达观点仅字面含义，非引战，非反串，仅为个人感想，个人娱乐，无任何衍生含义内容，不代表任何其他团体、个人，无任何隐喻，暗示，反串，碰瓷，蹭热度等想法。本人家庭和睦安康、无任何心理或精神疾病，智力为正常水平，完整接受了九年义务教育。本人观点及言论仅代表我个人一点浅薄的看法，非专业学术内容仅为个人理解，部分内容仅为猜测，不代表实际情况，与本人所在群体、父母亲朋、所在国家、省、市、地区无关，如有不同观点欢迎礼貌讨论、指正。本言论不含有对任何群体的歧视，不含有任何挑起对立的含义。本人认知范围浅薄，无专业团队，内容偏个人想法，如有误会歧义欢迎指正。无任何恶意侵权行为，如果引用、化用了他人观点我会尽量表明出处，如有侵权请证明关联性，本人会尽快处理。本人的表达能力一般，如果文字过于欠揍绝非恶意鄙视某个人、团体、组织、群体。如有您不认可的内容纯属手滑，绝非故意针对你个人或你所在群体、团体、组织。本人神经天马行空，常常脱离常识，如有歧义欢迎指正。本人为地球人，热爱地球文化文明，严格遵守所在地区的法律法规，绝无任何反人类倾向，从未进行过时空穿梭行为。本人承诺未向三体发送过地球坐标，未向任何外星人、异次元文明、平行宇宙、其它宇宙、平行宇宙透露过地球信息，从未撞断不周山，从未教唆纣王建造酒池肉林，从未派遣徐福东渡，从未残害忠良，从未勾结任何帝国主义军队，从未杀害奥匈帝国皇室。本人个人性别为男性，尊重男性、女性和其他性少数群体，坚定支持男女平等，男女两字的排序不分前后。本人用词较为偏向网络口语，绝无任何恶意，绝无任何将严肃话题娱乐话的意图。本人承诺热爱动物、植物、对人体和自然环境有益的、无害的微生物，如若把人比喻成某种动物、植物或微生物仅为通俗调侃，绝无任何践踏人类人格、尊严、人权等意图，也绝无歧视该动物、植物、微生物的意图。本人素质为平均素质，发表言论不具备任何专业性，仅供参考。本人对自己发表内容会负所有责任。评论中如有不好言论，建议自行拉黑或举报处理，绝非我视而不见置之不理或认可不良内容。


def kill(source: CommandSource, dic: dict):
    server = source.get_server()
    source.reply('§c本服务有死亡掉落，使用!!kill confirm §c确认')
def kill_confirm(source: CommandSource, dic: dict):
    server = source.get_server()
    server.execute('kill '+source.player)
    server.say('§6 '+source.player+' §a在绝望中饮弹自尽了！')
def on_load(server, prev_module):
    

    server.register_help_message('!!kill','自杀')
    server.register_help_message('!!op', '成为op')

    builder = SimpleCommandBuilder()

    builder.command('!!op', get_op)
    builder.command('!!kill', kill)
    builder.command('!!kill confirm', kill_confirm)


    builder.register(server)


