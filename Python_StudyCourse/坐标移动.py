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
        # 向左移动将进行判断, 碰到墙壁进行反弹
        if new_x < legal_x[0]:
            if new_x // legal_x[0] >= 1:
                pos_x = legal_x[0] - (new_x % legal_x[0])
            else:
                pos_x = legal_x[0] - (new_x - legal_x[0])
        # 向右移动将进行判断, 碰到墙壁进行反弹
        elif new_x > legal_x[1]:
            if new_x // legal_x[1] >= 1:
                pos_x = legal_x[1] - (new_x % legal_x[1])
            else:
                pos_x = legal_x[1] - (new_x - legal_x[0])
        else:
            pos_x = new_x
        # 向下移动将进行判断, 碰到墙壁进行反弹
        if new_y < legal_y[0]:
            if new_y // legal_y[0] >= 1:
                pos_y = legal_y[0] - (new_y % legal_y[0])
            else:
                pos_y = legal_y[0] - (new_y - legal_y[0])
        # 向上移动将进行判断, 碰到墙壁进行反弹    
        elif new_y > legal_y[1]:
            if new_y // legal_y[1] >= 1:
                pos_y = legal_y[1] - (new_y % legal_y[1])
            else:               
                pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y
        return pos_x, pos_y
    return moving
if __name__ == '__main__':
    move = create()
    while True:
        about_direction = int(input('请输入移动方向(1表示往右走, -1标识往左走, 0表示不动):'))
        up_and_down_direction = int(input('请输入移动方向(1表示往上走, -1标识往下走, 0表示不动):'))
        step = int(input('移动多少步？'))
        result = move((about_direction, up_and_down_direction), step)
        print(f'x轴为{result[0]}, y轴为{result[1]}')