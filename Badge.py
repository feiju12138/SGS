import random
"""
身份牌类
"""
class Badge():

    """
    类别：
    0：主公
    1：忠臣
    2：反贼
    3：内奸
    """
    category = ""

    name = ""

    def __init__(self, category, name):
        self.category = category
        self.name = name

    def __str__(self):
        return f"这是一个身份牌对象\n" \
               f"类别 - {self.category}\n" \
               f"名称 - {self.name}\n" \
               f"---\n"

"""
身份牌堆类
"""
class BadgeStack():

    badge_array = []

    # 洗牌
    def rand_badge_array(self):
        # 创建一个缓存，用于临时存放打乱顺序的牌堆
        badge_array_cache = []
        while len(self.badge_array) != 0:
            # 每次随机弹出一个数据，并追加到缓存中
            badge_array_cache.append(self.badge_array.pop(random.randint(0, len(self.badge_array)-1)))
        # 循环结束后，把缓存赋值给原牌堆
        self.badge_array = badge_array_cache

    def __init__(self, num):
        if num == 5:
            self.badge_array.append(Badge(0, "主公"))
            self.badge_array.append(Badge(1, "忠臣"))
            self.badge_array.append(Badge(2, "反贼"))
            self.badge_array.append(Badge(2, "反贼"))
            self.badge_array.append(Badge(3, "内奸"))
            self.rand_badge_array()

        if num == 8:
            self.badge_array.append(Badge(0, "主公"))
            self.badge_array.append(Badge(1, "忠臣"))
            self.badge_array.append(Badge(1, "忠臣"))
            self.badge_array.append(Badge(2, "反贼"))
            self.badge_array.append(Badge(2, "反贼"))
            self.badge_array.append(Badge(2, "反贼"))
            self.badge_array.append(Badge(2, "反贼"))
            self.badge_array.append(Badge(3, "内奸"))
            self.rand_badge_array()


    def __str__(self):

        # for i in self.badge_array:
        #     print(i)

        return f"这是一个身份牌堆对象\n" \
               f"当前牌堆 - {self.badge_array}\n" \
               f"---\n"

