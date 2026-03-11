# 兵团PVP得分校验

def corpsScore(attack_num=0, defense_num=0, pk_num=0, attack_kill_num=0):
    
    '''
    # attack_num：进攻方兵团数量
    # defense_num：防守方兵团数量
    # attack_kill_num：攻击方击杀防守方兵团数量
    # each_kill_score : 每击杀一个兵团得分
    # each_killed_deduct_points: 每被击杀一个兵团扣分
    # serverCircle: PK服数量区间
    # legionBaseNum: 标准数
    # minPoint: 兵团战扣分上限
    '''
    result = []
    if not isinstance (attack_num, list) and not isinstance(defense_num, list) and not isinstance(pk_num, list) and not isinstance(attack_kill_num, list):
        attack_num = [attack_num]
        defense_num = [defense_num]
        pk_num = [pk_num]
        attack_kill_num = [attack_kill_num]
        attack_num_length = len(attack_num)
        defense_num_length = len(defense_num)
        pk_num_length = len(pk_num)
        attack_kill_num_length = len(attack_kill_num)
    else:
        attack_num_length = len(attack_num)
        defense_num_length = len(defense_num)
        pk_num_length = len(pk_num)
        attack_kill_num_length = len(attack_kill_num)

    if attack_num_length == defense_num_length == pk_num_length == attack_kill_num_length:
        for i in range(attack_num_length):
            serverCircle = [5,10,20]
            legionBaseNum = [15,25,30]
            minPoint = [[15, 30], [25, 50], [30, 60]]
            if pk_num[i] <= serverCircle[0]:
                index = 0
            elif  pk_num[i] > serverCircle[0] and  pk_num[i] <= serverCircle[1] :
                index = 1
            elif pk_num[i] <= serverCircle[2] or pk_num[i] > serverCircle[2]:
                index = 2

            each_kill_score  = 2       #每击杀一个兵团得分
            each_killed_deduct_points = 1  #每被击杀一个兵团扣分
            attack_score = None          # 进攻方得分
            defense_deduct_points = None    # 防守方扣分


            # 判断是否有轮空分数
            if defense_num[i] < legionBaseNum[index]:
                Wheel_space_separation = legionBaseNum[index] - defense_num[i]
                attack_score = Wheel_space_separation + attack_kill_num[i]
                if attack_kill_num[i] == defense_num[i]:
                    defense_deduct_points = attack_kill_num[i] + Wheel_space_separation
                else:
                    defense_deduct_points = attack_kill_num[i]
            else:
                if attack_kill_num[i] < legionBaseNum[index]:
                    attack_score = attack_kill_num[i]
                    defense_deduct_points = attack_kill_num[i]
                if attack_kill_num[i] >= legionBaseNum[index]:
                    attack_score = max(legionBaseNum[index], min(attack_num[i], attack_kill_num[i]))
                    defense_deduct_points = min(legionBaseNum[index], attack_kill_num[i])
                    
            attack_score = attack_score * each_kill_score
            defense_deduct_points = defense_deduct_points * each_killed_deduct_points

            if defense_deduct_points > minPoint[index][0]:
                defense_deduct_points = minPoint[index][0]
            print('进攻方得分:', attack_score, '防守方扣分:', defense_deduct_points)
            result.append((attack_score, defense_deduct_points))
    return result


# corpsScore 方法共4个参数
# 1：[进攻方兵团数量] 
# 2：[防守方兵团数量]
# 3：[pk服数量]
# 4：[攻击方击杀防守方兵团数量]


result = corpsScore([5, 10, 30], [10, 15, 30], [2, 3, 4], [10, 15, 30])




# 国战门客攻击，血量计算
def stateFight_servantAttribute(ability=0, level=0, longmai_atk=0,longmai_hp=0, bonus=0, CriticalStrike=1):
    atk = ability * 100 + longmai_atk
    hp = ability * (level * level + level + 98) / 10 + longmai_hp
    hurt_max = atk * 1.1 * bonus * CriticalStrike
    hurt = atk * 1 * bonus * CriticalStrike
    hurt_min = atk * 0.9 * bonus * CriticalStrike

    return atk, hp, hurt_max, hurt, hurt_min


#result = stateFight_servantAttribute(21260, 200, bonus=1.2)
#print(f'门客攻击力: {result[0]}, 门客血量: {result[1]}, 实际伤害(最大): {result[2]}, 实际伤害(正常): {result[3]}, 实际伤害(最小): {result[4]}')

            
# 国战门客提供建造进度
def stateFight_BuildValue(servant_ability, buff=1):

    default_value = 300   # 基础进度， 走配置
    default_point = 300   # 基础贡献， 走配置
    # 门客资质范围， 走配置
    abilityRange = [[0, 100, 10, 0], [101, 250, 15, 0.2], [251, 500, 20, 0.4], [501, 1000, 25, 0.6], [1001, 5000, 30, 0.8], [5001, 999999, 35, 1]]
    for i in abilityRange:
        if servant_ability >= i[0] and servant_ability <= i[1]:
            add_value = i[2]
            add_point = i[3]
    provide_value = add_value * 20 + (default_value * buff)
    provide_point = default_point * (1 + add_point)
    return provide_value, provide_point
#result = BuildValue(1001)
#print(f'派遣门客进行建造，增加{result[0]}进度, 增加{result[1]}贡献值')
    
# 国战门客派遣侦察得分
def stateFight_scoutScore(servant_ability):
    # 门客资质范围， 走配置
    default_score = 100
    abilityRange = [[0, 1000, 0], [1001, 2000, 20], [2001, 3000, 40], [3001, 4000, 60], [4001, 5000, 80], [5001, 999999, 100]]
    for i in abilityRange:
        if servant_ability >= i[0] and servant_ability <= i[1]:
            add_score = i[2]
            
    provide_score = default_score + add_score
    return provide_score

#result = stateFight_scoutScore(2222)
#print(f'派遣门客进行侦察，增加{result}分')

        



