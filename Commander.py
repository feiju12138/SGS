"""
武将类
"""
class Commander():

    # 编号
    id = ""

    """
    国家：
    0：没有势力
    1：魏势力
    2：蜀势力
    3：吴势力
    4：群势力
    """
    nation = ""

    # 武将名
    name = ""

    # 血上限
    blood = ""

    # 武将技能列表
    skill = []

    def __init__(self, id, nation, name, blood, skill):
        self.id = id
        self.nation = nation
        self.name = name
        self.blood = blood
        self.skill = skill

    def __str__(self):
        return f"---\n" \
               f"这是一个武将类\n" \
               f"编号 = {self.id}\n" \
               f"国家 = {self.nation}\n" \
               f"武将名 = {self.name}\n" \
               f"血上限 = {self.blood}\n" \
               f"技能列表 = {self.skill}\n"
