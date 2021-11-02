"""
用户基本信息
"""
class User():

    # 编号
    id = ""

    # 用户名（用于登录，不可重复）
    username = ""

    # 昵称（用于展示，可以重复）
    nickname = ""

    # 性别
    sex = ""

    # 等级
    level = ""


    def __init__(self, id, username, nickname, sex, level):
        self.id = id
        self.username = username
        self.nickname = nickname
        self.sex = sex
        self.level = level

    def __str__(self):
        return f"---\n" \
               f"\n" \
               f"编号 - {self.id}\n" \
               f"用户名 - {self.username}\n" \
               f"昵称 - {self.nickname}\n" \
               f"性别 - {self.sex}\n" \
               f"等级 - {self.level}\n"
