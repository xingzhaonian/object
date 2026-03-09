import lupa

def load_lua_config(file):
    # 读取lua文件
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 匹配纯表内容
    start = content.find('{')
    end = content.rfind('}') + 1
    table_content = content[start:end]

    # 创建lua 虚拟机
    lua = lupa.LuaRuntime()

    # 执行lua 代码
    lua.execute(f"config = {table_content}")

    # 返回全局变量(执行 config = {table_content})
    result_config = lua.globals().config
    return result_config


def lua_to_py(lua_table):
    
    # 将 lua 配置转为 python dict
    if isinstance(lua_table, (int, float, str, bool, type(None))):
        return lua_table
    result = {}
    for key in lua_table.keys():
        value = lua_table[key]
        if hasattr(value, 'keys'):
            result[key] = lua_to_py(value)
        else:
            result[key] = value
    return result


def use_lua_func(file):
    # eval() 和 execute() 的作用不一样
    # 要结果 → 用 eval()
    # 要执行 → 用 execute()
    # 有 return → 用 eval()
    # 有 = 赋值 → 用 execute()

    # 读取lua文件

    with open(file, 'r', encoding='utf-8') as f:
        read_result = f.read()

    # 创建lua虚拟机, 支持函数调用时返回多个值自动解包
    lua = lupa.LuaRuntime(unpack_returned_tuples=True)

    # 执行lua代码, 返回lua虚拟机, 可以在python 中调用; 使用lua.eval('要调用的函数(参数)')
    lua.execute(read_result)
    return lua


#lua = use_lua_func('test_lua.lua')
#result = lua.eval('add(5, 9)')
#print(result)

