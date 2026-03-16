import requests
import json

def call_deepseek(prompt, api_key):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"]

if __name__ == "__main__":
    API_KEY = "你的DeepSeek API Key"  # 替换为你的真实Key
    user_input = input("请输入你的问题：")
    reply = call_deepseek(user_input, API_KEY)
    print("DeepSeek 回复：", reply)
