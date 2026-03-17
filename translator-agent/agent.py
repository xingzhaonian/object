# agent.py
"""
Agent核心模块 - 整合翻译和Item配置管理功能
"""

import os
import re
from openai import OpenAI
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class SimpleAgent:
    """智能Agent - 支持翻译和游戏配置管理"""
    
    def __init__(self, name="智能助手"):
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
        
        # 系统提示词 - 定义Agent的行为和可用技能
        self.system_prompt = f"""你是{name}，一个智能助手，拥有以下技能：

1. 🌍 **翻译技能** - 可以将文字翻译成多种语言
   - 触发词：翻译、怎么说、用英文、用中文、translate
   - 示例："翻译：你好世界"、"用英文怎么说：谢谢"

2. 🎮 **游戏配置管理** - 管理游戏Item配置表
   - 触发词：新增、添加、查询、修改、删除、列出、物品、item
   - 示例：
     * 新增武器 "屠龙刀" 攻击力200 描述"神兵"
     * 查询 item_001
     * 列出所有物品
     * 修改 屠龙刀 攻击力=300
     * 删除 屠龙刀 (需要确认)

请根据用户输入，选择合适的技能来处理，并给出友好、清晰的回复。
"""
    
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
        Agent的思考过程：分析用户意图，决定使用哪个技能
        
        Args:
            user_input: 用户输入
        
        Returns:
            dict: 包含行动计划的字典
        """
        user_input_lower = user_input.lower()
        
        # ========== 翻译技能关键词 ==========
        translate_keywords = ["翻译", "怎么说", "用英文", "用中文", "用英语", 
                              "translate", "how to say", "in english", "in chinese"]
        
        for keyword in translate_keywords:
            if keyword in user_input_lower:
                # 提取要翻译的文本
                text_to_translate = user_input
                for k in translate_keywords:
                    text_to_translate = text_to_translate.replace(k, "").strip()
                
                # 判断目标语言
                target_lang = "英文"  # 默认
                if "用中文" in user_input_lower or "用汉语" in user_input_lower:
                    target_lang = "中文"
                elif "用英文" in user_input_lower or "用英语" in user_input_lower:
                    target_lang = "英文"
                elif "用日文" in user_input_lower or "用日语" in user_input_lower:
                    target_lang = "日文"
                elif "用韩文" in user_input_lower or "用韩语" in user_input_lower:
                    target_lang = "韩文"
                elif "用法文" in user_input_lower or "用法语" in user_input_lower:
                    target_lang = "法文"
                elif "用德文" in user_input_lower or "用德语" in user_input_lower:
                    target_lang = "德文"
                
                return {
                    "type": "use_skill",
                    "skill": "translator",
                    "action": "translate",
                    "params": {
                        "text": text_to_translate,
                        "target_lang": target_lang
                    }
                }
        
        # ========== 游戏配置管理技能关键词 ==========
        config_keywords = ["新增", "添加", "查询", "修改", "删除", "列出", "物品", "item", 
                          "武器", "防具", "消耗品", "材料"]
        
        # 检查是否是配置管理相关指令
        is_config = False
        for keyword in config_keywords:
            if keyword in user_input_lower:
                is_config = True
                break
        
        if is_config and "item_config" in self.skills:
            # 判断具体操作类型
            if "新增" in user_input or "添加" in user_input:
                return {
                    "type": "use_skill",
                    "skill": "item_config",
                    "action": "add",
                    "params": {"input": user_input}
                }
            elif "查询" in user_input:
                return {
                    "type": "use_skill",
                    "skill": "item_config",
                    "action": "query",
                    "params": {"input": user_input}
                }
            elif "修改" in user_input:
                return {
                    "type": "use_skill",
                    "skill": "item_config",
                    "action": "update",
                    "params": {"input": user_input}
                }
            elif "删除" in user_input:
                return {
                    "type": "use_skill",
                    "skill": "item_config",
                    "action": "delete",
                    "params": {"input": user_input}
                }
            elif "列出" in user_input or "列表" in user_input:
                return {
                    "type": "use_skill",
                    "skill": "item_config",
                    "action": "list",
                    "params": {"input": user_input}
                }
            else:
                # 可能是模糊查询或其他操作
                return {
                    "type": "use_skill",
                    "skill": "item_config",
                    "action": "auto",
                    "params": {"input": user_input}
                }
        
        # 没有匹配到任何技能，用LLM直接对话
        return {
            "type": "direct_response",
            "skill": None,
            "action": None,
            "params": {}
        }
    
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
            skill = self.skills[action["skill"]]
            
            # ===== 翻译技能执行 =====
            if action["skill"] == "translator":
                return self._execute_translation(skill, action["params"])
            
            # ===== Item配置技能执行 =====
            elif action["skill"] == "item_config":
                return self._execute_item_config(skill, action["action"], action["params"]["input"])
        
        # ===== 直接对话 =====
        return self._chat_with_llm(user_input)
    
    def _execute_translation(self, skill, params):
        """执行翻译"""
        text = params.get("text", "")
        target_lang = params.get("target_lang", "英文")
        
        if not text:
            return "请告诉我需要翻译什么内容"
        
        # 调用LLM进行翻译
        return self._translate_with_llm(text, target_lang)
    
    def _translate_with_llm(self, text, target_lang):
        """使用LLM进行翻译"""
        try:
            # 构建翻译提示
            prompt = f"请将以下文本翻译成{target_lang}，只返回翻译结果，不要有任何额外内容：\n{text}"
            
            # 调用DeepSeek API
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个专业的翻译助手，只返回翻译结果，不添加任何解释。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            translation = response.choices[0].message.content
            
            return f"【{target_lang}翻译】\n{translation}"
            
        except Exception as e:
            return f"翻译时出错：{str(e)}"
    
    def _execute_item_config(self, skill, action, user_input):
        
    # 新增物品
        if action == "add":
            print(f"🔍 解析添加指令: {user_input}")
            
            # 提取类型 - 匹配"新增"或"添加"后面的第一个词
            type_match = re.search(r'(?:新增|添加)\s*(\S+)', user_input)
            if not type_match:
                return "请指定物品类型，例如：新增武器 \"屠龙刀\""
            item_type = type_match.group(1)
            
            # 提取名称 - 支持双引号、单引号、中文引号
            name_match = re.search(r'[“"\'][\s]*([^“"\'”]+)[\s]*[“"\'”]', user_input)
            if not name_match:
                return "请用引号括起物品名称，例如：新增武器 \"屠龙刀\""
            name = name_match.group(1).strip()
            
            # 初始化参数字典
            kwargs = {
                "攻击力": 0,
                "描述": "",
                "掉落概率": 0.1,
                "掉落数量": 1,
                "购买价": 100,
                "出售价": 50,
                "材料1": "",
                "材料2": ""
            }
            
            # 逐个解析参数（支持中英文冒号、等号、空格）
            
            # 1. 解析攻击力
            attack_match = re.search(r'攻击力[：:=\s]*(\d+)', user_input)
            if attack_match:
                kwargs["攻击力"] = int(attack_match.group(1))
                print(f"📌 攻击力: {kwargs['攻击力']}")
            
            # 2. 解析购买价
            buy_match = re.search(r'购买价[：:=\s]*(\d+)', user_input)
            if buy_match:
                kwargs["购买价"] = int(buy_match.group(1))
                print(f"📌 购买价: {kwargs['购买价']}")
            
            # 3. 解析出售价
            sell_match = re.search(r'出售价[：:=\s]*(\d+)', user_input)
            if sell_match:
                kwargs["出售价"] = int(sell_match.group(1))
                print(f"📌 出售价: {kwargs['出售价']}")
            
            # 4. 解析掉落概率（支持小数）
            drop_rate_match = re.search(r'掉落概率[：:=\s]*([\d.]+)', user_input)
            if drop_rate_match:
                kwargs["掉落概率"] = float(drop_rate_match.group(1))
                print(f"📌 掉落概率: {kwargs['掉落概率']}")
            
            # 5. 解析掉落数量
            drop_count_match = re.search(r'掉落数量[：:=\s]*(\d+)', user_input)
            if drop_count_match:
                kwargs["掉落数量"] = int(drop_count_match.group(1))
                print(f"📌 掉落数量: {kwargs['掉落数量']}")
            
            # 6. 解析材料1
            material1_match = re.search(r'材料1[：:=\s]*([^,\s]+)', user_input)
            if material1_match:
                kwargs["材料1"] = material1_match.group(1).strip()
                print(f"📌 材料1: {kwargs['材料1']}")
            
            # 7. 解析材料2
            material2_match = re.search(r'材料2[：:=\s]*([^,\s]+)', user_input)
            if material2_match:
                kwargs["材料2"] = material2_match.group(1).strip()
                print(f"📌 材料2: {kwargs['材料2']}")
            
            # 8. 解析描述（特殊处理，可能包含空格和标点）
            desc_match = re.search(r'描述[：:=\s]*[“"\'][\s]*([^“"\'”]+)[\s]*[“"\'”]', user_input)
            if desc_match:
                kwargs["描述"] = desc_match.group(1).strip()
                print(f"📌 描述: {kwargs['描述'][:30]}...")
            else:
                # 尝试另一种格式：描述:内容（无引号）
                desc_match2 = re.search(r'描述[：:=\s]*([^,，]+)', user_input)
                if desc_match2 and len(desc_match2.group(1)) < 50:  # 避免匹配到太长的内容
                    kwargs["描述"] = desc_match2.group(1).strip()
                    print(f"📌 描述: {kwargs['描述']}")
            
            print(f"\n📦 最终解析结果:")
            print(f"  名称: {name}")
            print(f"  类型: {item_type}")
            for k, v in kwargs.items():
                print(f"  {k}: {v}")
            
            # 调用skill的add_item方法
            print(f"\n📦 调用 add_item 的参数:")
            print(f"  name={name}")
            print(f"  item_type={item_type}")
            print(f"  attack={kwargs['攻击力']}")
            print(f"  description={kwargs['描述']}")
            print(f"  drop_rate={kwargs['掉落概率']}")
            print(f"  drop_count={kwargs['掉落数量']}")
            print(f"  buy_price={kwargs['购买价']}")
            print(f"  sell_price={kwargs['出售价']}")
            print(f"  material1={kwargs['材料1']}")
            print(f"  material2={kwargs['材料2']}")
            print("-" * 40)

            # 调用skill的add_item方法
            return skill.add_item(
                name=name,
                item_type=item_type,
                attack=kwargs["攻击力"],
                description=kwargs["描述"],
                drop_rate=kwargs["掉落概率"],
                drop_count=kwargs["掉落数量"],
                buy_price=kwargs["购买价"],
                sell_price=kwargs["出售价"],
                material1=kwargs["材料1"],
                material2=kwargs["材料2"]
            )
        
        # 其他action处理保持不变...
        elif action == "query":
            # 查询物品
            match = re.search(r'查询\s*([^\s]+)', user_input)
            if match:
                return skill.query_item(match.group(1))
            return "请指定要查询的物品ID或名称"
        
        elif action == "list":
            # 列出物品
            if "武器" in user_input:
                return skill.list_items("武器")
            elif "防具" in user_input:
                return skill.list_items("防具")
            elif "消耗品" in user_input:
                return skill.list_items("消耗品")
            else:
                return skill.list_items()
        
        elif action == "update":
            # 修改物品（简化版，你可以根据需要扩展）
            return "修改功能开发中..."
        
        elif action == "delete":
            # 删除物品
            match = re.search(r'删除\s*([^\s]+)', user_input)
            if match:
                item = match.group(1)
                if "确认" in user_input or "yes" in user_input.lower():
                    return skill.delete_item(item, confirm=True)
                else:
                    return skill.delete_item(item)
            return "请指定要删除的物品"
        
        return "我不理解这个配置指令"
    
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
    
    def get_skills_info(self):
        """获取所有已注册技能的信息"""
        info = [f"📚 已注册技能 ({len(self.skills)}):"]
        for name, skill in self.skills.items():
            if hasattr(skill, 'info'):
                skill_info = skill.info()
                info.append(f"  - {name}: {skill_info.get('description', '无描述')}")
            else:
                info.append(f"  - {name}")
        return "\n".join(info)