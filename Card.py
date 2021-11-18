import random
"""
卡牌类
"""
class Card:

    """
    类别：
    100：基本牌
        101：杀
        102：闪
        103：桃
        104：酒
        105：火杀
        106：雷杀

    200：非延时锦囊
        201：决斗
        202：过河拆桥
        203：顺手牵羊
        204：无中生有
        205：借刀杀人
        206：无懈可击
        207：南蛮入侵
        208：万箭齐发
        209：桃园结义
        210：五谷丰登
        211：火攻
        212：铁索连环

    300：延时锦囊
        301：乐不思蜀
        302：闪电
        303：兵粮寸断

    400：武器牌
        401：诸葛连弩 - 方片A、梅花A - 范围1
        402：青釭剑 - 黑桃6 - 范围2
        403：雌雄双股剑 - 黑桃2 - 范围2
        404：贯石斧 - 方片5 - 范围3
        405：青龙偃月刀 - 黑桃5 - 范围3
        406：丈八蛇矛 - 黑桃Q - 范围3
        407：方天画戟 - 方片Q - 范围4
        408：麒麟弓 - 红桃5 - 范围5
        409：古锭刀 - 黑桃A - 范围2
        410：朱雀羽扇 - 方片A - 范围4
        411：寒冰剑 - 黑桃2 - 范围2

    500：防具牌
        501；八卦阵 - 黑桃2、梅花2
        502：白银狮子 - 梅花A
        503：藤甲 - 黑桃2、梅花2
        504：仁王盾 - 梅花2

    600：+马
        601: 爪黄飞电 - 红桃K
        602: 的卢 - 梅花5
        603: 绝影 - 黑桃5
        604: 骅骝 - 方片K

    700：-马
        701: 赤兔 - 红桃5
        702: 紫骍 - 方片K
        703: 大宛 - 黑桃K

    """
    category = ""

    """
    名称
    """
    name = ""

    """
    花色
    """
    color = ""

    """
    点数
    """
    points = ""

    """
    点数权值
    """
    points_weight = ""

    """
    武器的范围
    """
    scope = ""

    # 根据点数赋值权值
    def weight(self):
        if self.points == "A":
            self.points_weight = 1
        elif self.points == "2":
            self.points_weight = 2
        elif self.points == "3":
            self.points_weight = 3
        elif self.points == "4":
            self.points_weight = 4
        elif self.points == "5":
            self.points_weight = 5
        elif self.points == "6":
            self.points_weight = 6
        elif self.points == "7":
            self.points_weight = 7
        elif self.points == "8":
            self.points_weight = 8
        elif self.points == "9":
            self.points_weight = 9
        elif self.points == "10":
            self.points_weight = 10
        elif self.points == "J":
            self.points_weight = 11
        elif self.points == "Q":
            self.points_weight = 12
        elif self.points == "K":
            self.points_weight = 13

    def __init__(self):
        self.color = ["红桃♥", "方片♦", "黑桃♠", "梅花♣"][random.randint(0, 3)]
        self.points = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][random.randint(0, 12)]
        self.weight()

    def __str__(self):
        return f"这是一个卡牌对象\n" \
               f"类别 - {self.category}\n" \
               f"名称 - {self.name}\n" \
               f"花色 - {self.color}\n" \
               f"点数 - {self.points}\n" \
               f"点数权值 - {self.points_weight}\n" \
               f"武器的攻击范围 - {self.scope}\n" \
               f"---"

"""
杀101
"""
class Sha(Card):

    def __init__(self):
        self.category = 101
        self.name = "杀"
        super().__init__()

"""
闪102
"""
class Shan(Card):

    def __init__(self):
        self.category = 102
        self.name = "闪"
        super().__init__()

"""
桃103
"""
class Tao(Card):

    def __init__(self):
        self.category = 103
        self.name = "桃"
        super().__init__()

"""
酒104
"""
class Jiu(Card):

    def __init__(self):
        self.category = 104
        self.name = "酒"
        super().__init__()

"""
火杀105
"""
class HuoSha(Card):

    def __init__(self):
        self.category = 105
        self.name = "火杀"
        super().__init__()


"""
雷杀106
"""
class LeiSha(Card):

    def __init__(self):
        self.category = 106
        self.name = "雷杀"
        super().__init__()

"""
决斗201
"""
class JueDou(Card):

    def __init__(self):
        self.category = 201
        self.name = "决斗"
        super().__init__()

"""
过河拆桥202
"""
class GuoHeChaiQiao(Card):

    def __init__(self):
        self.category = 202
        self.name = "过河拆桥"
        super().__init__()

"""
顺手牵羊203
"""
class ShunShouQianYang(Card):

    def __init__(self):
        self.category = 203
        self.name = "顺手牵羊"
        super().__init__()

"""
无中生有204
"""
class WuZhongShengYou(Card):

    def __init__(self):
        self.category = 204
        self.name = "无中生有"
        super().__init__()

"""
借刀杀人
"""
class JieDaoShaRen(Card):

    def __init__(self):
        self.category = 205
        self.name = "借刀杀人"
        super().__init__()

"""
无懈可击206
"""
class WuXieKeJi(Card):

    def __init__(self):
        self.category = 206
        self.name = "无懈可击"
        super().__init__()

"""
南蛮入侵207
"""
class NanManRuQin(Card):

    def __init__(self):
        self.category = 207
        self.name = "南蛮入侵"
        super().__init__()

"""
万箭齐发208
"""
class WanJianQiFa(Card):

    def __init__(self):
        self.category = 208
        self.name = "万箭齐发"
        super().__init__()

"""
桃园结义209
"""
class TaoYuanJieYi(Card):

    def __init__(self):
        self.category = 209
        self.name = "桃园结义"
        super().__init__()

"""
五谷丰登210
"""
class WuGuFengDeng(Card):

    def __init__(self):
        self.category = 210
        self.name = "五谷丰登"
        super().__init__()

"""
火攻211
"""
class HuoGong(Card):

    def __init__(self):
        self.category = 211
        self.name = "火攻"
        super().__init__()

"""
铁索连环212
"""
class TieSuoLianHuan(Card):

    def __init__(self):
        self.category = 212
        self.name = "铁索连环"
        super().__init__()

"""
乐不思蜀301
"""
class LeBuSiShu(Card):

    def __init__(self):
        self.category = 301
        self.name = "乐不思蜀"
        super().__init__()

"""
闪电302
"""
class ShanDian(Card):

    def __init__(self):
        self.category = 302
        self.name = "闪电"
        super().__init__()

"""
兵粮寸断303
"""
class BingLiangCunDuan(Card):

    def __init__(self):
        self.category = 303
        self.name = "兵粮寸断"
        super().__init__()

"""
诸葛连弩401
"""
class ZhuGeLianNu(Card):

    def __init__(self):
        self.category = 401
        self.name = "诸葛连弩"
        self.scope = 1
        super().__init__()

"""
青釭剑402
"""
class QingGangJian(Card):

    def __init__(self):
        self.category = 402
        self.name = "青釭剑"
        self.scope = 2
        super().__init__()

"""
雌雄双股剑403
"""
class CiXiongShuangGuJian(Card):

    def __init__(self):
        self.category = 403
        self.name = "雌雄双股剑"
        self.scope = 2
        super().__init__()

"""
贯石斧404
"""
class GuanShiFu(Card):

    def __init__(self):
        self.category = 404
        self.name = "贯石斧"
        self.scope = 3
        super().__init__()

"""
青龙偃月刀405
"""
class QingLongYanYueDao(Card):

    def __init__(self):
        self.category = 405
        self.name = "青龙偃月刀"
        self.scope = 3
        super().__init__()

"""
丈八蛇矛406
"""
class ZhangBaSheMao(Card):

    def __init__(self):
        self.category = 406
        self.name = "丈八蛇矛"
        self.scope = 3
        super().__init__()

"""
方天画戟407
"""
class FangTianHuaJi(Card):

    def __init__(self):
        self.category = 407
        self.name = "方天画戟"
        self.scope = 4
        super().__init__()

"""
麒麟弓408
"""
class QiLinGong(Card):

    def __init__(self):
        self.category = 408
        self.name = "麒麟弓"
        self.scope = 5
        super().__init__()

"""
古锭刀409
"""
class GuDingDao(Card):

    def __init__(self):
        self.category = 409
        self.name = "古锭刀"
        self.scope = 2
        super().__init__()

"""
朱雀羽扇410
"""
class ZhuQueYuShan(Card):

    def __init__(self):
        self.category = 410
        self.name = "朱雀羽扇"
        self.scope = 4
        super().__init__()

"""
寒冰剑411
"""
class HanBingJian(Card):

    def __init__(self):
        self.category = 411
        self.name = "寒冰剑"
        self.scope = 2
        super().__init__()

"""
八卦阵501
"""
class BaGuaZhen(Card):

    def __init__(self):
        self.category = 501
        self.name = "八卦阵"
        super().__init__()

"""
白银狮子502
"""
class BaiYinShiZi(Card):

    def __init__(self):
        self.category = 502
        self.name = "白银狮子"
        super().__init__()

"""
藤甲503
"""
class TengJia(Card):

    def __init__(self):
        self.category = 503
        self.name = "藤甲"
        super().__init__()

"""
仁王盾504
"""
class RenWangDun(Card):

    def __init__(self):
        self.category = 504
        self.name = "仁王盾"
        super().__init__()

"""
爪黄飞电601
"""
class ZhuaHuangFeiDian(Card):

    def __init__(self):
        self.category = 601
        self.name = "爪黄飞电"
        super().__init__()

"""
的卢602
"""
class DiLu(Card):

    def __init__(self):
        self.category = 602
        self.name = "的卢"
        super().__init__()

"""
绝影603
"""
class JueYing(Card):

    def __init__(self):
        self.category = 603
        self.name = "绝影"
        super().__init__()

"""
骅骝604
"""
class HuaLiu(Card):

    def __init__(self):
        self.category = 604
        self.name = "骅骝"
        super().__init__()

"""
赤兔701
"""
class ChiTu(Card):

    def __init__(self):
        self.category = 701
        self.name = "赤兔"
        super().__init__()

"""
紫骍702
"""
class ZiXing(Card):

    def __init__(self):
        self.category = 702
        self.name = "紫骍"
        super().__init__()

"""
大宛703
"""
class DaWan(Card):

    def __init__(self):
        self.category = 703
        self.name = "大宛"
        super().__init__()



"""
摸牌堆类
"""
class CardStack():

    __card_array = []

    # 洗牌
    def rand_card_array(self):
        # 创建一个缓存，用于临时存放打乱顺序的牌堆
        card_array_cache = []
        # 遍历以前的卡牌列表
        while len(self.__card_array) != 0:
            # 每次随机弹出一个数据，并追加到缓存中
            card_array_cache.append(self.__card_array.pop(random.randint(0, len(self.__card_array)-1)))
        # 循环结束后，把缓存赋值给原牌堆
        self.__card_array = card_array_cache

    # 从牌堆顶拿一张牌
    def popCardFromTop(self):
        return self.__card_array.pop()

    # 从牌堆顶底一张牌
    def popCardFromBottom(self):
        return self.__card_array.pop(0)

    def __init__(self):

        for i in range(80):
            self.__card_array.append(ZhuGeLianNu())
            self.__card_array.append(JieDaoShaRen())
            self.__card_array.append(Sha())
            self.__card_array.append(LeiSha())
            self.__card_array.append(HuoSha())


        # 基本牌100
        for i in range(20):
            # self.__card_array.append(Sha())
            # self.__card_array.append(Shan())
            # self.__card_array.append(Tao())
            # self.__card_array.append(Jiu())
            # self.__card_array.append(HuoSha())
            # self.__card_array.append(LeiSha())
            pass

        # 非延时锦囊200
        for i in range(10):
            # self.__card_array.append(JueDou()) # 已自测
            # self.__card_array.append(GuoHeChaiQiao()) # 已自测
            # self.__card_array.append(ShunShouQianYang()) # 已自测
            # self.__card_array.append(WuZhongShengYou()) # 已自测
            # self.__card_array.append(JieDaoShaRen()) # 已自测
            # self.__card_array.append(WuXieKeJi()) # 已自测
            # self.__card_array.append(NanManRuQin()) # 已自测
            # self.__card_array.append(WanJianQiFa()) # 已自测
            # self.__card_array.append(TaoYuanJieYi()) # 已自测
            # self.__card_array.append(WuGuFengDeng()) # 已自测
            # self.__card_array.append(HuoGong())
            # self.__card_array.append(TieSuoLianHuan()) # 已自测
            pass

        # 延时锦囊300
        for i in range(5):
            # self.__card_array.append(LeBuSiShu())
            # self.__card_array.append(ShanDian())
            # self.__card_array.append(BingLiangCunDuan())
            pass

        # 武器牌400
        for i in range(2):
            # self.__card_array.append(ZhuGeLianNu())
            # self.__card_array.append(QingGangJian())
            # self.__card_array.append(CiXiongShuangGuJian())
            # self.__card_array.append(GuanShiFu())
            # self.__card_array.append(QingLongYanYueDao())
            # self.__card_array.append(ZhangBaSheMao())
            # self.__card_array.append(FangTianHuaJi())
            # self.__card_array.append(QiLinGong())
            # self.__card_array.append(GuDingDao())
            # self.__card_array.append(ZhuQueYuShan())
            # self.__card_array.append(HanBingJian())
            pass

        # 防具牌500
        for i in range(3):
            # self.__card_array.append(BaGuaZhen())
            # self.__card_array.append(BaiYinShiZi())
            # self.__card_array.append(TengJia())
            # self.__card_array.append(RenWangDun())
            pass

        # +马600
        for i in range(5):
            # self.__card_array.append(ZhuaHuangFeiDian())
            # self.__card_array.append(DiLu())
            # self.__card_array.append(JueYing())
            # self.__card_array.append(HuaLiu())
            pass

        # -马700
        for i in range(5):
            # self.__card_array.append(ChiTu())
            # self.__card_array.append(ZiXing())
            # self.__card_array.append(DaWan())
            pass

        # 洗牌
        self.rand_card_array()

    def __str__(self):

        for i in self.__card_array:
            print(i)

        return f"这是一个摸牌堆对象\n" \
               f"当前牌堆 - {self.__card_array}\n" \
               f"当前牌堆卡牌总数 - {len(self.__card_array)}\n" \
               f"---"

"""
出牌堆类
"""
class DiscardStack():

    __card_array = []

    # 向出牌堆顶部添加一张牌
    def addCardForArray(self, card):
        self.__card_array.append(card)

    def __init__(self):

        pass

    def __str__(self):
        return f"---\n" \
               f"这是一个出牌堆对象\n" \
               f"当前牌堆 - {self.__card_array}\n" \
               f"当前牌堆卡牌总数 - {len(self.__card_array)}\n"


