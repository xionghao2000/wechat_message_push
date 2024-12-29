import requests
import datetime

def send_wechat(msg):
    token = '5c722f6c8bf441f88387b8e37e2e846c'#前边复制到那个token
    title = 'title1'
    content = msg
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    print(url)
    r = requests.get(url=url)
    print(r.text)
 
if __name__ == '__main__':
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    msg = f'{today} 点饭啦点饭啦～🍜🍚🌽🍔'
    send_wechat(msg)