"""
用户基本信息
"""
class User():

    def __init__(self, id, username, nickname, sex, level):

        # 编号
        self.id = id

        # 用户名（用于登录，不可重复）
        self.username = username

        # 昵称（用于展示，可以重复）
        self.nickname = nickname

        # 性别
        self.sex = sex

        # 等级
        self.level = level

    def __str__(self):
        return f"---\n" \
               f"\n" \
               f"编号 - {self.id}\n" \
               f"用户名 - {self.username}\n" \
               f"昵称 - {self.nickname}\n" \
               f"性别 - {self.sex}\n" \
               f"等级 - {self.level}\n"
