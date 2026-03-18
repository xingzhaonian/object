# agent.py
import json
from openai import OpenAI
from typing import Dict, Any, List
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class SmartAgent:
    """真正智能的AI Agent"""
    
    def __init__(self, name="智能助手"):
        self.name = name
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
        )
        self.tools: Dict[str, Dict] = {}
        self.conversation_history = []
        self.max_history = 10
    
    def register_tool(self, name: str, func: callable, description: str, parameters: Dict):
        """注册工具"""
        self.tools[name] = {
            "func": func,
            "description": description,
            "parameters": parameters
        }
        print(f"✅ 工具已注册: {name}")
    
    def _build_system_prompt(self) -> str:
        """构建系统提示"""
        tools_desc = []
        for name, info in self.tools.items():
            params = ", ".join([f"{p}: {desc}" for p, desc in info["parameters"].items()])
            tools_desc.append(f"- {name}({params}): {info['description']}")
        
        tools_str = "\n".join(tools_desc)
        
        return f"""你是{self.name}，一个智能助手，可以理解用户的自然语言并调用工具完成任务。

可用工具：
{tools_str}

工作流程：
1. 理解用户的真实意图
2. 如果需要澄清，可以反问用户
3. 规划如何完成任务
4. 调用合适的工具
5. 用自然语言回复用户

请始终用JSON格式回复，格式如下：
{{
    "type": "chat",
    "content": "回复内容"
}}
或
{{
    "type": "ask",
    "question": "追问的问题"
}}
或
{{
    "type": "tool",
    "name": "工具名",
    "params": {{"参数名": "参数值"}}
}}
或
{{
    "type": "multi",
    "steps": [
        {{"type": "tool", "name": "工具1", "params": {{...}}}},
        {{"type": "tool", "name": "工具2", "params": {{...}}}}
    ]
}}
"""
    
    def process(self, user_input: str) -> str:
        """处理用户输入"""
        print(f"\n🤔 {self.name} 正在思考...")
        
        messages = [
            {"role": "system", "content": self._build_system_prompt()},
            *self.conversation_history[-self.max_history:],
            {"role": "user", "content": user_input}
        ]
        
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                temperature=0.3,
                max_tokens=1000
            )
            
            ai_response = json.loads(response.choices[0].message.content)
            result = self._execute(ai_response)
            
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": result})
            
            return result
            
        except Exception as e:
            return f"❌ 处理出错: {str(e)}"
    
    def _execute(self, ai_response: Dict) -> str:
        """执行AI的决策"""
        
        if ai_response["type"] == "chat":
            return ai_response["content"]
        
        elif ai_response["type"] == "ask":
            return f"❓ {ai_response['question']}"
        
        elif ai_response["type"] == "tool":
            tool_name = ai_response["name"]
            params = ai_response["params"]
            
            if tool_name not in self.tools:
                return f"❌ 未知工具: {tool_name}"
            
            try:
                tool_func = self.tools[tool_name]["func"]
                result = tool_func(**params)
                return f"✅ {result}"
            except Exception as e:
                return f"❌ 工具执行失败: {str(e)}"
        
        elif ai_response["type"] == "multi":
            results = []
            for i, step in enumerate(ai_response["steps"], 1):
                step_result = self._execute(step)
                results.append(f"【步骤{i}】{step_result}")
            return "\n".join(results)
        
        else:
            return f"❌ 未知响应类型: {ai_response['type']}"