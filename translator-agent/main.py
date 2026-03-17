"""
主程序 - 翻译Agent的入口
"""

from agent import SimpleAgent
from skills.translator import TranslationSkill
import sys

def main():
    """主函数"""
    print("=" * 50)
    print("🤖 智能翻译助手 v1.0")
    print("=" * 50)
    print("支持的语言：中文、英文、日文、韩文、法文、德文、西班牙文")
    print("输入示例：")
    print("  - 翻译：你好，世界")
    print("  - 用英文怎么说：你好")
    print("  - 把这个翻译成日文：谢谢")
    print("  - 退出/exit 结束程序")
    print("=" * 50)
    
    # 1. 创建Agent
    agent = SimpleAgent(name="翻译官")
    
    # 2. 创建并注册翻译技能
    translator = TranslationSkill(target_lang="英文")  # 默认目标语言为英文
    agent.register_skill("translator", translator)
    
    print("\n✅ Agent初始化完成，随时为你服务！\n")
    
    # 3. 对话循环
    while True:
        try:
            # 获取用户输入
            user_input = input("\n👤 你: ").strip()
            
            # 检查退出条件
            if user_input.lower() in ["退出", "exit", "quit", "q"]:
                print("👋 再见！感谢使用翻译助手")
                break
            
            if not user_input:
                continue
            
            # 处理用户输入
            response = agent.process(user_input)
            
            # 输出响应
            print(f"\n🤖 {agent.name}: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 程序被中断，再见！")
            break
        except Exception as e:
            print(f"\n❌ 发生错误: {str(e)}")
            print("请重试或输入'退出'结束程序")

def quick_test():
    """快速测试函数"""
    print("运行快速测试...")
    
    # 创建Agent
    agent = SimpleAgent()
    translator = TranslationSkill()
    agent.register_skill("translator", translator)
    
    # 测试用例
    test_cases = [
        "翻译：你好，世界",
        "用英文怎么说：我爱你",
        "把这个翻译成日文：谢谢",
        "你好吗？",  # 非翻译请求
    ]
    
    for test in test_cases:
        print(f"\n📝 测试输入: {test}")
        response = agent.process(test)
        print(f"💬 响应: {response}")
        print("-" * 30)

if __name__ == "__main__":
    # 如果带参数 --test 则运行测试
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        quick_test()
    else:
        main()