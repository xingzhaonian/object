#   递归

#   1：相信递归调用已经正确工作（递归信仰）
#   2：只关注当前层（一层的视角）
#   3：从最简单情况开始（递归三要素）
#   4：黑盒思维法（最实用）
#   把递归调用当作一个已经写好的、绝对正确的函数来用。
#   不需要想：递归怎么展开、有多少层、每层怎么返回


def flatten_dict(d, parent_key=''):
    items = []
    
    for k, v in d.items():


        if parent_key:
            new_key = f"{parent_key}.{k}"
        else:
            new_key = k
        if isinstance(v, dict):
            # ✅ 关键思维：这里不要想 flatten_dict 内部怎么实现！
            # ✅ 就当它是别人写好的、功能正确的函数
            # ✅ 你只需要知道：给它一个字典和前缀，它返回扁平化字典
            
            sub_result = flatten_dict(v, new_key)  # 魔法黑盒
            items.extend(sub_result.items())  # 黑盒返回字典，我取键值对
        else:
            items.append((new_key, v))  # 简单情况自己处理
    
    return dict(items)











'''
def recursive_func(data):
    # 1️⃣ 终止条件（必须有！）
    if 满足最简单情况:
        return 最简单情况的答案
    
    # 2️⃣ 缩小问题规模（向终止条件靠近）
    更小问题 = 把原问题变小一点
    
    # 3️⃣ 递归调用 + 组合结果
    子结果 = recursive_func(更小问题)
    return 用某种方式组合子结果
'''