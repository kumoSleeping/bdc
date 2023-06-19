from flask import Flask, render_template, request
import requests
import random
import html
import json
import ast
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    global send, au, co
    mm = request.form.get('mm')  # 获取用户输入的谱面ID
    send = ' '  # 定义一个默认值为空的send变量

    url = 'https://bestdori.com/api/post/details?id={}'.format(mm)
    response = requests.get(url, verify=False)
    bd_json = response.json()
    # print(bd_json)
    
    # {"result":false,"code":"REQUEST_INVALID"}
    
    # return '🐱喵喵喵。我是一只小猫，你愿意和我做朋友吗？'
    if bd_json["result"] == False:
        return render_template('index2.html', result=html.unescape(send), title='🐱喵喵喵。我是一只小猫，你愿意和我做朋友吗？', bd_json='无', chart_json='无', au='无', co='无', au_ayachan='无', co_ayachan='无', is_find='无')
    if 'chart' not in bd_json['post']:
        return render_template('index2.html', result=html.unescape(send), title='🐱喵喵喵。我是一只小猫，你愿意和我做朋友吗？', bd_json='无', chart_json='无', au='无', co='无', au_ayachan='无', co_ayachan='无', is_find='无')
    
    chart = bd_json['post']['chart']
    chart_json = str(chart).replace(' ', '').replace("'", '"').replace("True", 'true')
    # print(chart_json)

    au_ayachan = f"https://proxy.ayachan.fun/assets/bestdori/{mm}/audio"
    co_ayachan = f"https://proxy.ayachan.fun/assets/bestdori/{mm}/cover"

    title = f'{bd_json["post"]["title"]} - {bd_json["post"]["artists"]} \n'
    try:
        au = bd_json["post"]["song"]["audio"]
    except:
        au = '无'
        pass
    try:
        co = bd_json["post"]["song"]["cover"]
    except:
        co = '无'
        pass

    return render_template('index2.html', result=html.unescape(send), title=title, bd_json=bd_json, chart_json=chart_json, au=au, co=co, au_ayachan=au_ayachan, co_ayachan=co_ayachan, is_find='有')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12783, debug=True, use_reloader=True)
