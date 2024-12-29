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
    
    # 使用 HTML 格式化内容
    content = """
    <h1>点饭啦点饭啦～ 🍜🍚🌽🍔</h1>
    """.format(date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    send_wechat(token, title, content)