origin = (0, 0)
legal_x = [-100, 100]
legal_y = [-100, 100]

def create():
    pos_x=0
    pos_y=0
    def moving(direction, step):
        nonlocal pos_x
        nonlocal pos_y
        new_x = pos_x + direction[0] * step
        new_y = pos_y + direction[1] * step
        # 向左移动将进行判断, 超出范围将在左侧范围内反弹
        if new_x < legal_x[0]:
            if new_x // legal_x[0] >= 1:
                pos_x = legal_x[0] - (new_x % legal_x[0])
            else:
                pos_x = legal_x[0] - (new_x - legal_x[0])
        # 向右移动将进行判断, 超出范围将在左侧范围内反弹        
        elif new_x > legal_x[1]:
            if new_x // legal_x[1] >= 1:
                pos_x = legal_x[1] - (new_x % legal_x[1])
            else:
                pos_x = legal_x[1] - (new_x - legal_x[0])
        else:
            pos_x = new_x
        # 向下移动将进行判断, 超出范围将在左侧范围内反弹
        if new_y < legal_y[0]:
            if new_y // legal_y[0] >= 1:
                pos_y = legal_y[0] - (new_y % legal_y[0])
            else:
                pos_y = legal_y[0] - (new_y - legal_y[0])
        # 向上移动将进行判断, 超出范围将在左侧范围内反弹        
        elif new_y > legal_y[1]:
            if new_y // legal_y[1] >= 1:
                pos_y = legal_y[1] - (new_y % legal_y[1])
            else:               
                pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y
        print(pos_x, pos_y)
        return pos_x, pos_y
    return moving

move = create()
move((1, 0), 20)
move((0, 1), 120)
move((1, -1), 88)