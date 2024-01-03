import requests
import time
import json
import webbrowser

# 设置请求的URL
url = "https://mix.whxh.com.cn/api/register/new/dateschedulelist?_route=h187&login_access_token=1702020233288-3B4872AEB5470CDEBD1BF8"

headers = {
    'Host': 'mix.whxh.com.cn',
    'Connection': 'keep-alive',
    'Content-Length': '201',
    'client': 'patient',
    'content-type': 'application/x-www-form-urlencoded',
    'channel': 'wx_xcx',
    'uid': '4571449596982132808',
    'his-id': '187',
    'Hc-Src-Hisid': '187',
    'uuid': '0b3621bb-1887-4a1f-9ae3-e7fa737ef532',
    'device-id': '',
    'request-id': 'beb90070-c2ec-442b-a202-1d3d302737bd',
    'Hc-Proj-Info': 'project/his-wxapp;type/miniapp;ch/wechat;ver/mix;',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.44(0x18002c27) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wxd07219591f885e68/67/page-frame.html',
}

data = {
    'hisId': '187',
    'platformId': '187',
    'platformSource': '3',
    'subSource': '1',
    'doctorId': '1-914',
    'subHisId': '18701',
    'deptId': '203_121',
    't': '202312',
    'sign': 'A8ACB41E7590A1F1A03401C08EDF1BB5',
    'login_access_token': '1702020233288-3B4872AEB5470CDEBD1BF8',
}

def send_request():
    try:
        response = requests.post(url, headers=headers, data=data)
        # 输出响应结果
        # print(response.text)
        re =  json.loads(response.text)
        for item in re["data"]["scheduleList"]:
            # print('检查每个项目的 status 是否为 1')
            if item["status"] != "2" and item["status"] != "0":
                print("找到 status 为 1 的项目:")
                webbrowser.open('http://www.baidu.com/', new=0, autoraise=True)
                print(item)
    except Exception as e:
        print(f"Error: {e}")

        
# 定时发送请求，可以根据实际情况调整时间间隔
while True:
    print('send_request')
    send_request()
    time.sleep(5)  # 每隔60秒发送一次请求