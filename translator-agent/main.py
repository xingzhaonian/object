# main.py
import sys
import os
from pathlib import Path

# 获取当前文件所在目录
current_dir = Path(__file__).parent.absolute()
print(f"📁 当前目录: {current_dir}")

# 添加项目根目录到系统路径
sys.path.insert(0, str(current_dir))

# 导入模块
from agent import SmartAgent

# 从 tools 文件夹导入 ItemTools（类名匹配了！）
try:
    from tools.item_config import ItemTools
    print("✅ 成功导入 ItemTools")
except ImportError as e:
    print(f"❌ 导入 ItemTools 失败: {e}")
    print(f"🔍 请确保文件存在: {current_dir}\\tools\\item_config.py")
    raise

# 简单版登录工具
class SimpleLoginTools:
    """简单登录工具"""
    
    def batch_login(self, servers: list, users: list):
        """批量登录"""
        results = []
        for server in servers:
            for user in users:
                results.append(f"✅ {user}@{server} 登录成功")
        return "批量登录完成:\n" + "\n".join(results)
    
    def login_test_users(self, servers: list):
        """登录测试用户"""
        test_users = [f"test{i}" for i in range(1, 6)]
        return self.batch_login(servers, test_users)

def main():
    print("=" * 60)
    print("🤖 智能AI助手")
    print("=" * 60)
    print("你可以这样说话：")
    print("  - 新增武器 屠龙刀 攻击力999")
    print("  - 查询屠龙刀")
    print("  - 列出所有物品")
    print("  - 登录服务器67,68 用户cxk04,cxk03")
    print("=" * 60)
    
    # 创建Agent
    agent = SmartAgent("小智")
    
    # 初始化物品工具
    try:
        item_tools = ItemTools(config_dir="config")
        print("✅ 物品工具初始化成功")
    except Exception as e:
        print(f"❌ 物品工具初始化失败: {e}")
        return
    
    # 初始化登录工具
    login_tools = SimpleLoginTools()
    
    # 注册物品工具
    agent.register_tool(
        name="add_item",
        func=item_tools.add_item,
        description="新增游戏物品",
        parameters={
            "name": "物品名称",
            "item_type": "物品类型（武器/防具/消耗品）",
            "attack": "攻击力数值",
            "description": "物品描述"
        }
    )
    
    agent.register_tool(
        name="query_item",
        func=item_tools.query_item,
        description="查询物品信息",
        parameters={
            "name_or_id": "物品名称或ID"
        }
    )
    
    agent.register_tool(
        name="list_items",
        func=item_tools.list_items,
        description="列出所有物品",
        parameters={}
    )
    
    # 注册登录工具
    agent.register_tool(
        name="batch_login",
        func=login_tools.batch_login,
        description="批量登录服务器",
        parameters={
            "servers": "服务器ID列表，如 [67,68]",
            "users": "用户名列表，如 ['cxk04','cxk03']"
        }
    )
    
    agent.register_tool(
        name="login_test_users",
        func=login_tools.login_test_users,
        description="登录测试用户（test1-test5）",
        parameters={
            "servers": "服务器ID列表"
        }
    )
    
    print("\n✅ Agent初始化完成，开始对话吧！\n")
    
    # 对话循环
    while True:
        try:
            user_input = input("\n👤 你: ").strip()
            
            if user_input.lower() in ["exit", "quit", "退出"]:
                print("👋 再见！")
                break
            
            if not user_input:
                continue
            
            response = agent.process(user_input)
            print(f"\n🤖 {agent.name}: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except Exception as e:
            print(f"\n❌ 错误: {e}")

if __name__ == "__main__":
    main()