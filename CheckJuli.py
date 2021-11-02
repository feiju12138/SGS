# 实际距离
def ShijiJuli(player_from, player_to):

    # 从上家找距离
    sum_left = 1
    point = player_from.left_player
    while point.location != player_to.location:
        point = point.left_player
        sum_left += 1
    # 从下家找距离
    sum_right = 1
    point = player_from.right_player
    while point.location != player_to.location:
        point = point.right_player
        sum_right += 1
    sum = 0
    # 找到较小的那一个数字作为距离
    if sum_left<sum_right:
        sum = sum_left
    else:
        sum = sum_right

    # 起点-马修正距离
    if player_from.equipment["horse-"]!="":
        sum -= 1
    # 终点+马修正距离
    if player_to.equipment["horse+"]!="":
        sum += 1

    return sum

# 攻击距离
def GoJiJuLi(player_from, player_to):

    sum = ShijiJuli(player_from, player_to)

    # 武器修正距离
    if player_from.equipment["arms"]!="":
        sum -= player_from.equipment["arms"].scope

    return sum