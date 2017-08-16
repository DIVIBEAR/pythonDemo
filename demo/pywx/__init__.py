# encoding=utf-8
from flask import Flask,request
import urllib.request
import json

appID="......"
AppSecret="......"
url_code = "https://api.weixin.qq.com/sns/oauth2/access_token?appid={appid}&secret={appsecret}&code={code}&grant_type=authorization_code"
url_retoken = "https://api.weixin.qq.com/sns/oauth2/refresh_token?appid={appid}&grant_type=refresh_token&refresh_token={refresh_token}"
url_info = "https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}&lang=zh_CN"
app = Flask(__name__)
#获取微信服务号code
@app.route('/pywx/getCode')
def getCode():
    code = request.args.get('code')
    if code:
        accessToken = urllib.request.Request(url_code.format(appid=appID, appsecret=AppSecret, code=code))
        res_data = urllib.request.urlopen(accessToken)
        res = res_data.read().decode('utf-8')
        res_json=json.loads(res)#转成json
        access_token=res_json["access_token"]
        refresh_token=res_json["refresh_token"]
        openid = res_json["openid"]
        getRefreshToken=urllib.request.Request(url_retoken.format(appid=appID,refresh_token=refresh_token))
        res_data = urllib.request.urlopen(getRefreshToken)
        res_reToken = res_data.read().decode('utf-8')
        res_json = json.loads(res_reToken)  # 转成json
        access_token = res_json["access_token"]
        getUserInfo = urllib.request.Request(url_info.format(access_token=access_token,openid=openid))
        res_data = urllib.request.urlopen(getUserInfo)
        res = res_data.read().decode('utf-8')
        return res

if __name__ == '__main__':
    #app.run(host="服务器地址",post=端口号,debug模式)
    app.run(port=7099,debug=True)