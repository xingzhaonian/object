# main.py
"""
主程序 - 整合翻译和游戏配置管理功能
"""

from agent import SimpleAgent
from skills.translator import TranslationSkill
from skills.item_config import ItemConfigSkill

def print_welcome():
    """打印欢迎信息"""
    print("=" * 60)
    print("🤖 多功能智能助手 v2.0")
    print("=" * 60)
    print("\n📦 **已加载技能：**")
    print("  🌍 翻译技能 - 多语言翻译")
    print("  🎮 游戏配置管理 - 管理Item配置表")
    print("\n📝 **使用示例：**")
    print("\n🌍 **翻译功能：**")
    print('  - 翻译：你好世界')
    print('  - 用英文怎么说：谢谢')
    print('  - 把这个翻译成日文：我爱你')
    print("\n🎮 **游戏配置管理：**")
    print('  - 新增武器 "屠龙刀" 攻击力200 描述"神兵"')
    print('  - 新增防具 "黄金甲" 购买价500')
    print('  - 查询 item_001')
    print('  - 查询 木剑')
    print('  - 列出所有物品')
    print('  - 列出武器')
    print('  - 修改 屠龙刀 攻击力=300')
    print('  - 删除 屠龙刀 (需要确认)')
    print("\n💬 **其他功能：**")
    print('  - 普通聊天（没有触发词时会直接对话）')
    print('  - 输入 "exit" 或 "退出" 结束程序')
    print('  - 输入 "skills" 查看已注册技能')
    print("=" * 60)

def main():
    """主函数"""
    print_welcome()
    
    # 1. 创建Agent
    agent = SimpleAgent(name="智能助手")
    
    # 2. 注册翻译技能
    translator = TranslationSkill()
    agent.register_skill("translator", translator)
    
    # 3. 注册游戏配置管理技能
    item_config = ItemConfigSkill("config/game_config.xlsx")
    agent.register_skill("item_config", item_config)
    
    print(f"\n✅ Agent初始化完成！")
    print(f"📁 配置文件: config/game_config.xlsx")
    print(f"💾 备份目录: config/backups/")
    
    # 4. 对话循环
    while True:
        try:
            user_input = input("\n👤 你: ").strip()
            
            # 检查退出条件
            if user_input.lower() in ["退出", "exit", "quit", "q"]:
                print("\n👋 再见！感谢使用智能助手")
                break
            
            # 显示技能信息
            if user_input.lower() == "skills":
                print(f"\n{agent.get_skills_info()}")
                continue
            
            if not user_input:
                continue
            
            # 处理用户输入
            response = agent.process(user_input)
            
            # 输出响应
            print(f"\n🤖 {agent.name}: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except Exception as e:
            print(f"\n❌ 发生错误: {str(e)}")
            print("请检查错误信息，或输入'退出'结束程序")

def quick_test():
    """快速测试函数"""
    print("=" * 50)
    print("🚀 快速测试模式")
    print("=" * 50)
    
    # 创建Agent
    agent = SimpleAgent("测试助手")
    
    # 注册技能
    translator = TranslationSkill()
    agent.register_skill("translator", translator)
    
    item_config = ItemConfigSkill("config/test_config.xlsx")
    agent.register_skill("item_config", item_config)
    
    # 测试用例
    test_cases = [
        "翻译：你好，世界",
        "用英文怎么说：我爱你",
        "新增武器 '测试剑' 攻击力100",
        "列出所有物品",
        "你好吗？",
    ]
    
    print("\n开始测试...\n")
    
    for i, test in enumerate(test_cases, 1):
        print(f"📝 测试 {i}: {test}")
        response = agent.process(test)
        print(f"💬 响应: {response}")
        print("-" * 40)
    
    print("\n✅ 测试完成！")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        quick_test()
    else:
        main()