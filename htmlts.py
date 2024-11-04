import re
import requests
from bs4 import BeautifulSoup
import hashlib
import random
import os
import time

# 读取 help.html 文件内容
with open("help.html", "r", encoding="utf-8") as file:
    content = file.read()

# 使用正则表达式处理所有标签内部的多余空白字符和换行
# 替换所有标签内的内容，去除多余空白和换行
content = re.sub(r'>\s*([\s\S]*?)\s*<', lambda m: '>' + re.sub(r'\s+', ' ', m.group(1)).strip() + '<', content)

# 将替换后的内容写入到 htmlv2.html 文件
with open("htmlv2.html", "w", encoding="utf-8") as file:
    file.write(content)

print("处理完成，结果已写入到 htmlv2.html。")

# 设置代理，如果需要请手动打开
# os.environ["http_proxy"] = "http://127.0.0.1:10101"  # 或 SOCKS 端口  
# os.environ["https_proxy"] = "http://127.0.0.1:10101"  # 或 SOCKS 端口  

# 设置百度翻译 API 的相关参数
APP_ID = ''  # 替换为你的 App ID
SECRET_KEY = ''  # 替换为你的 Secret Key
URL = "http://api.fanyi.baidu.com/api/trans/vip/translate"

# 读取处理后的 HTML 文件内容
with open("htmlv2.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# 使用 BeautifulSoup 解析 HTML 内容
soup = BeautifulSoup(html_content, "html.parser")

# 获取所有需要翻译的文本节点
text_elements = [element for element in soup.find_all(text=True) if isinstance(element, str) and element.strip()]
total_elements = len(text_elements)
print('文件解析完毕，开始翻译...')

# 遍历每个需要翻译的文本元素
for index, element in enumerate(text_elements):
    query = element.strip()  # 确保查询文本没有多余空格
    salt = str(random.randint(32768, 65536))
    sign = APP_ID + query + salt + SECRET_KEY
    sign = hashlib.md5(sign.encode()).hexdigest()

    params = {
        'q': query,
        'from': 'en',  # 源语言
        'to': 'zh',  # 目标语言
        'appid': APP_ID,
        'salt': salt,
        'sign': sign,
    }

    try:
        response = requests.get(URL, params=params)
        result = response.json()

        if 'trans_result' in result:
            translated_text = result['trans_result'][0]['dst']
            # 将节点文本直接替换为翻译后的内容
            element.replace_with(translated_text)
            print(f"正在翻译第 {index + 1}/{total_elements} 段文本：成功")
        else:
            print(f"翻译失败: {result.get('error_msg', '未知错误')} (段落 {index + 1})")
    except Exception as e:
        print(f"请求失败: {e} (段落 {index + 1})")

    # 延迟一小段时间，避免被限制
    time.sleep(0.5)

# 保存翻译后的 HTML
with open("translated_help_preview.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

print("翻译完成，结果已保存到 'translated_help_preview.html' 文件中")
