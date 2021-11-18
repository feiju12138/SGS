"""
玩家类
"""
class Player():

    # 当前手牌
    __card_array = []

    # 获取所有手牌的数量
    def lenCardForArray(self):
        return len(self.__card_array)

    # 移除指定位置的手牌
    def popCardForArray(self, index):
        return self.__card_array.pop(index)

    # 移除指定手牌
    def popCard(self, card):
        for i in range(len(self.__card_array)):
            if self.__card_array[i]==card:
                return self.__card_array.pop(i)
        print("DEBUG: 移除手牌失败")
        return None

    # 移除任意牌（含手牌、装备牌、延时锦囊牌）
    def popCardForAll(self, card):
        for i in range(len(self.__card_array)):
            if self.__card_array[i]==card:
                return self.__card_array.pop(i)
        if self.equipment["arms"] != "" and self.equipment["arms"]==card:
                c = card
                self.equipment["arms"] = ""
                return c
        if self.equipment["armor"] != "" and self.equipment["armor"]==card:
                c = card
                self.equipment["armor"] = ""
                return c
        if self.equipment["horse+"] != "" and self.equipment["horse+"]==card:
                c = card
                self.equipment["horse+"] = ""
                return c
        if self.equipment["horse-"] != "" and self.equipment["horse-"]==card:
                c = card
                self.equipment["horse-"] = ""
                return c
        if self.mark_skil_bag["lebusishu"] != "" and self.equipment["lebusishu"]==card:
                c = card
                self.mark_skil_bag["lebusishu"] = ""
                return c
        if self.mark_skil_bag["shandian"] != "" and self.equipment["shandian"]==card:
                c = card
                self.mark_skil_bag["shandian"] = ""
                return c
        if self.mark_skil_bag["bingliangcunduan"] != "" and self.equipment["bingliangcunduan"]==card:
                c = card
                self.mark_skil_bag["bingliangcunduan"] = ""
                return c
        print("DEBUG: 移除牌失败")
        return None

    # 获取指定位置的手牌
    def showCardForArray(self, index):
        return self.__card_array[index]

    # 获取所有手牌
    def listCardForArray(self):
        return self.__card_array

    # 添加一张手牌
    def addCardForArray(self, card):
        self.__card_array.append(card)

    def __init__(self, user, badge, commander, card_array):

        # 用户信息
        self.user = user

        # 身份信息
        self.badge = badge

        # 武将信息
        self.commander = commander

        # 体力
        self.blood = commander.blood

        # 手牌
        self.__card_array = card_array

        # 装备区
        self.equipment = {
            "arms": "",
            "armor": "",
            "horse+": "",
            "horse-": ""
        }

        # 延时锦囊标记
        self.mark_skil_bag = {
            # 乐不思蜀
            "lebusishu": "",
            # 闪电
            "shandian": "",
            # 兵粮寸断
            "bingliangcunduan": ""
        }

        # 卡牌相关标记
        self.mark_card = {
            # 铁索连环
            "tiesuolianhuan": False
        }

        # 技能相关标记
        self.mark_skill = {

        }

        # 当前回合标记
        self.mark_bout = {
            # 当前回合是否出过杀
            "sha": False,
            # 酒
            "jiu": False

        }

        # 阵亡标记
        self.is_die = False

        # 座位编号
        self.location = ""

        # 下家（右手边的玩家）
        self.right_player = ""

        # 上家（左手边的玩家）
        self.left_player = ""


    def __str__(self):

        return f"---\n" \
               f"这是一个玩家类\n" \
               f"用户信息 - {self.user.nickname}\n" \
               f"身份信息 - {self.badge.name}\n" \
               f"位置号 - {self.location}\n" \
               f"武将信息 - {self.commander.name}\n" \
               f"当前血量 - {self.blood}\n" \
               f"当前手牌 - {self.__card_array}\n"
