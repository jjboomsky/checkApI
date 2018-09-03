import requests
import json
from bs4 import BeautifulSoup
import time,threading
import matplotlib.pyplot as plt

user_result = {
         '大单' : 0
        ,'小单' : 0
        ,'大双' : 0
        ,'小双' : 0
        ,'大' : 0
        ,'小' : 0
        ,'单' : 0
        ,'双' : 0
    }

def make_user_login(roomid):
    issue_id = 2326621
    for i in range(50):
        headers = {'Accept': 'application/json,application/xml,application/xhtml+xml,text/html;q=0.9,image/webp,*/*;q=0.8'
            , 'Accept-Encoding': 'gzip, deflate'
            , 'Accept-Language': 'zh-CN,zh'
            ,'Authorization': 'Bearer YNnlc05P8Hj8JE6AlSgIXd2su9zD2jZ69ORY3RoIgJ3MlMVppcpwzoSl8Ayb5Cj6VKWz64bak3vZHKTRf-l5gEabU9pnsY-Y1ZpooPD-TYFye6X0-ae6bMoOeO-LwU8MKVD1JIbyEdsQIoce9BE_hAIWYCo-s4KnhGdGHA83O220oOg77dLHVPx-N4TMGSRZSvWL-K3tr1EGhp8kxwfY3w'
            , 'Connection': 'keep-alive'
            , 'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
            ,'User-Agent': 'Mozilla/5.0 (Linux; U; Android 7.1.1; zh-cn; OS105 Build/NGI77B) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            , 'Content-Length': '78'
            , 'Host': '45.61.241.170:5566'}
        datas = {
            'user_name' : 'b478934288'
            ,'password' : '123456a'
            ,'client_type' : '1'
            ,'client_Id' : 'Android/osborn/osborn:7.1.1/NGI77B/1534640972:user/dev-keys'
            ,'Client_Ip' : 'yiqpdRfXbR1Notuz99Oueg%3D%3D'
        }
        params = {
             'page' : i
             ,'roomid' : roomid
         }
        body = {
            'user_name': 'b478934288'
            , 'password': '123456a'
            , 'client_type': '1'
            , 'client_Id': 'Android/osborn/osborn:7.1.1/NGI77B/1534640972:user/dev-keys'
            , 'Client_Ip': 'yiqpdRfXbR1Notuz99Oueg%3D%3D'
        }
        session = requests.session()
        # url='http://45.61.241.170:5566/Api/User/login'
        # resp = session.post(url, data=datas, headers=headers)
        # rejson = resp.content.decode('utf-8')
        # redata = json.loads(rejson)[ 'result']
        s = session.get('http://45.61.243.44:5566/Api/Room/GetRoomTop10Chats' , params=params , headers=headers ,json=body )
        userdata = json.loads(s.content.decode('utf-8'))
        now_issue_id = int(userdata['result'][0]['body'].split('@')[0])
        if now_issue_id < issue_id:
            break
        else:
            issue_id = now_issue_id
            for result in userdata['result']:
                # 2326621 @ 双 @ 20 @ 7 @ 2.0 @ 204
                # 2326621 @ 大单 @ 33 @ 7 @ 4.2 @ 208
                # 2326621 @ 大 @ 50 @ 7 @ 2.0 @ 201
                data_split = result['body'].split('@')
                if data_split[1] == '大单':
                    user_result['大单'] += int(data_split[2])
                if data_split[1] == '小单':
                    user_result['小单'] += int(data_split[2])
                if data_split[1] == '大双':
                    user_result['大双'] += int(data_split[2])
                if data_split[1] == '小双':
                    user_result['小双'] += int(data_split[2])
                if data_split[1] == '大':
                    user_result['大'] += int(data_split[2])
                if data_split[1] == '小':
                    user_result['小'] += int(data_split[2])
                if data_split[1] == '单':
                    user_result['单'] += int(data_split[2])
                if data_split[1] == '双':
                    user_result['双'] += int(data_split[2])
                #print("{0}{1}{2}元".format(result['nickname'].center(30) , data_split[1].center(20), data_split[2].center(10)))
        time.sleep(0.2)
        print(user_result)
t = threading.Thread(target=make_user_login(38), name='make_user_data')
t.start()
key_list = list(user_result.keys())
value_list = list(user_result.values())
plt.bar(key_list,value_list)
# 指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
plt.show()