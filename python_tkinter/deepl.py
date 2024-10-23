import requests
import time
import random

deepl_url = 'https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs'
deepl_headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    "Content-Type":"application/json",
    "Content-Type": "application/json",
        }

tamptime = int(time.time() * 1000)


words = input('请输入要翻译的内容>>>')



payload = {
    "jsonrpc": "2.0",
    "method": "LMT_handle_jobs",
    "params": {
        "jobs": [
            {
                "kind": "default",
                "sentences": [
                    {
                        "text": words,  # 要翻译的文本
                        "id": 1,
                        "prefix": ""
                    }
                ],
                "raw_en_context_before": [],
                "raw_en_context_after": [],
                "preferred_num_beams": 4
            }
        ],
        "lang": {
            "target_lang": "EN",  # 目标语言：英语
            "preference": {
                "weight": {},
                "default": "default"
            },
            "source_lang_computed": "ZH"  # 源语言：中文
        },
        "priority": -1,
        "commonJobParams": {
            "quality": "fast",
            "regionalVariant": "en-US",
            "mode": "translate",
            "browserType": 1,
            "textType": "plaintext"
        },
        "timestamp": tamptime  # 使用当前时间戳
    },
    "id": int(random.randint(10**(8-1), 10**8 - 1))
}


response = requests.post(url=deepl_url, headers=deepl_headers, json=payload)

print(response)
print(response.headers)
print(response.text)