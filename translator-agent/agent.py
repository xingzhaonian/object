"""
Agent核心模块 - 负责任务规划、技能调用和LLM交互
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class SimpleAgent:
    """简单的Agent实现"""
    
    def __init__(self, name="翻译助手"):
        """
        初始化Agent
        
        Args:
            name: Agent名称
        """
        self.name = name
        self.skills = {}  # 技能存储字典
        self.conversation_history = []  # 对话历史
        
        # 初始化DeepSeek客户端
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
        )
        
        # 系统提示词 - 定义Agent的行为
        self.system_prompt = f"""你是{name}，一个智能翻译助手。
你的核心能力：
1. 理解用户的翻译需求
2. 调用翻译技能完成任务
3. 提供准确、自然的翻译结果

工作流程：
- 分析用户输入，判断是否需要翻译
- 如果需要翻译，调用translator技能
- 返回翻译结果给用户

请始终保持友好、专业的服务态度。"""
    
    def register_skill(self, skill_name, skill_instance):
        """
        注册技能到Agent
        
        Args:
            skill_name: 技能名称
            skill_instance: 技能实例
        """
        self.skills[skill_name] = skill_instance
        print(f"✅ 技能已注册: {skill_name}")
    
    def think(self, user_input):
        """
        Agent的思考过程：决定如何响应
        
        Args:
            user_input: 用户输入
        
        Returns:
            dict: 包含行动计划的字典
        """
        # 简单的规则判断
        # 在实际应用中，这里应该调用LLM进行更复杂的决策
        
        # 检查是否包含翻译关键词
        translate_keywords = ["翻译", "怎么说", "用英文", "用中文", "translate", "how to say"]
        
        action = {
            "type": "direct_response",  # 默认直接回复
            "skill": None,
            "params": {}
        }
        
        # 简单关键词匹配
        for keyword in translate_keywords:
            if keyword in user_input.lower():
                action["type"] = "use_skill"
                action["skill"] = "translator"
                
                # 简单解析目标语言
                if "英文" in user_input or "英语" in user_input:
                    action["params"]["target_lang"] = "英文"
                elif "中文" in user_input:
                    action["params"]["target_lang"] = "中文"
                elif "日文" in user_input or "日语" in user_input:
                    action["params"]["target_lang"] = "日文"
                else:
                    action["params"]["target_lang"] = None  # 使用默认
                
                break
        
        return action
    
    def execute(self, action, user_input):
        """
        执行行动计划
        
        Args:
            action: think()返回的行动计划
            user_input: 原始用户输入
        
        Returns:
            str: 执行结果
        """
        if action["type"] == "use_skill" and action["skill"] in self.skills:
            # 调用翻译技能
            skill = self.skills[action["skill"]]
            
            # 提取要翻译的文本
            # 简单实现：去除翻译指令部分
            text_to_translate = user_input
            for keyword in ["翻译", "怎么说", "用英文", "用中文", "translate"]:
                text_to_translate = text_to_translate.replace(keyword, "").strip()
            
            # 如果没有指定目标语言，使用默认
            target_lang = action["params"].get("target_lang")
            
            # 调用LLM进行翻译
            return self._translate_with_llm(text_to_translate, target_lang, skill)
        else:
            # 直接对话
            return self._chat_with_llm(user_input)
    
    def _translate_with_llm(self, text, target_lang, skill):
        """使用LLM进行翻译"""
        try:
            # 构建翻译提示
            if target_lang:
                prompt = f"请将以下文本翻译成{target_lang}，只返回翻译结果，不要有任何额外内容：\n{text}"
            else:
                prompt = f"请将以下文本翻译成英文，只返回翻译结果，不要有任何额外内容：\n{text}"
            
            # 调用DeepSeek API
            response = self.client.chat.completions.create(
                model="deepseek-chat",  # 或使用 "deepseek/deepseek-v3.2-speciale"
                messages=[
                    {"role": "system", "content": "你是一个专业的翻译助手，只返回翻译结果，不添加任何解释。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,  # 翻译需要较低的随机性
                max_tokens=1000
            )
            
            translation = response.choices[0].message.content
            
            # 构建友好的回复
            if target_lang:
                result = f"【{target_lang}翻译】\n{translation}"
            else:
                result = f"【翻译结果】\n{translation}"
            
            return result
            
        except Exception as e:
            return f"翻译时出错：{str(e)}"
    
    def _chat_with_llm(self, user_input):
        """普通对话"""
        try:
            # 构建消息历史
            messages = [
                {"role": "system", "content": self.system_prompt},
                *self.conversation_history[-5:],  # 最近5条对话历史
                {"role": "user", "content": user_input}
            ]
            
            # 调用DeepSeek API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            
            reply = response.choices[0].message.content
            
            # 保存到历史记录
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": reply})
            
            return reply
            
        except Exception as e:
            return f"对话时出错：{str(e)}"
    
    def process(self, user_input):
        """
        处理用户输入的完整流程
        
        Args:
            user_input: 用户输入
        
        Returns:
            str: Agent的响应
        """
        print(f"🤔 {self.name} 正在思考...")
        
        # 1. 思考
        action = self.think(user_input)
        print(f"📋 行动计划: {action}")
        
        # 2. 执行
        response = self.execute(action, user_input)
        
        return response

# 简单测试
if __name__ == "__main__":
    # 创建Agent
    agent = SimpleAgent("智能翻译官")
    
    # 测试思考过程
    test_input = "帮我翻译一下：你好，世界"
    action = agent.think(test_input)
    print(f"测试思考结果: {action}")