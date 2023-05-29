origin = (0, 0)
legal_x = [-5, 5]
legal_y = [-5, 5]

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
        return pos_x, pos_y
    return moving


move =  create()
print(move((0, 1), 6))
print(move((0, -1), 12))
print(move((-1, 0), 5))
print(move((1, 0), 37))
print(move((-1, 1), 77))
print(move((-1, -1), 38))
print(move((1, 1), 12))
print(move((1, -1), 56))