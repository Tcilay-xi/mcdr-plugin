import minecraft_data_api as api
from mcdreforged.api.all import *

dim_convert = {
    0 : 'minecraft:overworld',
    -1: 'minecraft:the_nether',
    1 : 'minecraft:the_end'
}


def get_dimension_translation_text(dim):
    dim_text = dim_convert.get(dim, '0')
    return dim_text

class coord:
    def __init__(self, x, y, z, dim, name=""):
        self.name = name
        self.dim_num = str(dim)
        self.dim = get_dimension_translation_text(int(dim))

        self.dim_text = '主世界' if self.dim_num == '0' else '地狱' if self.dim_num == '-1' else '末地'
        self.dim = dim_convert[self.dim_num]


        if self.dim_num == '0':
            self.x, self.y, self.z = map(str, (int(x), int(y), int(z)))
            self.dx, self.dy, self.dz = map(str, (int(x) // 8, int(y) // 8, int(z) // 8))
        elif self.dim_num == '-1':
            self.dx, self.dy, self.dz = map(str, (int(x), int(y), int(z)))
            self.x, self.y, self.z = map(str, (int(x) * 8, int(y) * 8, int(z) * 8))
        elif self.dim_num == "1":
            self.x, self.y, self.z = map(str, (int(x), int(y), int(z)))

    def text(self, type=""):
        match type:
            case "1":
                if self.dim_num == "0":
                    return f'[{self.x} ,{self.y} ,{self.z}]@{self.dim_text} --> [{self.dx},{self.dy},{self.dz}]@地狱'
                if self.dim_num == "-1":
                    return f'[{self.dx},{self.dy},{self.dz}]@{self.dim_text} --> [{self.x},{self.y},{self.z}]@主世界'
                if self.dim_num == "1":
                    return f'[{self.x},{self.y},{self.z}]@{self.dim_text}'
            case _:
                return f'[{self.x} ,{self.y} ,{self.z}]@{self.dim_text}'



@new_thread("step_query")
def get_player_pos(player):
    tpos = api.get_player_coordinate(player)
    dim = api.get_player_dimension(player)
    pos = coord(tpos.x,tpos.y,tpos.z,dim,player)
    return pos



type_convert = {
        0: "废弃传送门",
        1: "远古城市",
        2: "废弃矿井",
        3: "末地要塞",
        4: "沙漠神殿",
        5: "雪屋",
        6: "丛林神庙",
        7: "掠夺者前哨站",
        8: "沼泽小屋",
        9: "村庄",
        10: "林地府邸",
        11: "珊瑚礁",
        12: "海底神殿",
        13: "海底废墟",
        14: "沉船",
        15: "下界要塞",
        16: "末地城"
}

def trans_list():
    text = ''
    for i in type_convert:
        text += "|{0}-{1}".format(i,type_convert[i])
    text += "|"
    return text
    
def trans_type(type):
    return type_convert.get(int(type), "-1")

