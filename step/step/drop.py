def get_dimension_translation_text(dim):
    return dim_convert[dim]


class coord:
    x:str
    y:str
    z:str
    dx:str
    dy:str
    dz:str

    dim_num:str
    dim_text:str
    dim:str

    name:str
    def __init__(self, x, y, z, dim,name=""):
        self.name = name
        self.dim_num = str(dim)
        self.dim = get_dimension_translation_text(int(dim))
        if self.dim_num == "0":
            self.dim_text ='主世界'
            self.x = str(int(x))
            self.y = str(int(y))
            self.z = str(int(z))
            self.dx = str(int(x)/8)
            self.dy = str(int(y)/8)
            self.dz = str(int(z)/8)

        elif self.dim_num == "-1":
            self.dim_text ='地狱'
            self.dx=str(int(x))
            self.dy=str(int(y))
            self.dz=str(int(z))
            self.x = str(int(int(x)*8))
            self.y = str(int(int(y)*8))
            self.z = str(int(int(z)*8))

        elif self.dim_num == "1":
            self.dim_text ='末地'
            self.x = str(int(x))
            self.y = str(int(y))
            self.z = str(int(z))
    
    def text(self,type=""):
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
