import requests
import datetime

def send_wechat(token, title, content):
    url = "http://www.pushplus.plus/send"
    data = {
        "token": token,
        "title": title,
        "content": content,
        "template": "html"
    }
    response = requests.post(url, json=data)
    return response.json()

if __name__ == '__main__':
    title = "每周通知"
    token = "5c722f6c8bf441f88387b8e37e2e846c"
    content = "今天是周五，点饭啦点饭啦～🍜🍚🌽🍔"
    send_wechat(token, title, content)