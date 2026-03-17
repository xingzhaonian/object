"""
翻译技能模块 - 封装各种翻译引擎和功能
"""

class TranslationSkill:
    """翻译技能类"""
    
    def __init__(self, target_lang="中文"):
        """
        初始化翻译技能
        
        Args:
            target_lang: 默认目标语言
        """
        self.target_lang = target_lang
        self.supported_langs = ["中文", "英文", "日文", "韩文", "法文", "德文", "西班牙文"]
        
        # 技能描述 - 这是Agent用来发现技能的关键信息
        self.skill_description = {
            "name": "translator",
            "description": "多语言翻译技能，支持中、英、日、韩、法、德、西等语言互译",
            "version": "1.0.0"
        }
    
    def translate(self, text, source_lang="auto", target_lang=None):
        """
        执行翻译
        
        Args:
            text: 要翻译的文本
            source_lang: 源语言（auto表示自动检测）
            target_lang: 目标语言（默认使用初始化时设置的语言）
        
        Returns:
            dict: 包含翻译结果的字典
        """
        if target_lang is None:
            target_lang = self.target_lang
            
        # 构建翻译提示词
        prompt = self._build_prompt(text, source_lang, target_lang)
        
        return {
            "original": text,
            "translated": f"[模拟翻译] {text} -> {target_lang}",  # 这里后续会被大模型替换
            "source_lang": source_lang,
            "target_lang": target_lang,
            "prompt": prompt  # 保留prompt供Agent使用
        }
    
    def _build_prompt(self, text, source_lang, target_lang):
        """构建翻译提示词"""
        if source_lang == "auto":
            return f"请将以下文本翻译成{target_lang}，只返回翻译结果：\n{text}"
        else:
            return f"请将以下{source_lang}文本翻译成{target_lang}，只返回翻译结果：\n{text}"
    
    def get_supported_languages(self):
        """获取支持的语言列表"""
        return self.supported_langs
    
    def info(self):
        """返回技能信息"""
        return self.skill_description

# 简单的使用示例
if __name__ == "__main__":
    translator = TranslationSkill(target_lang="英文")
    result = translator.translate("你好，世界！")
    print(result)