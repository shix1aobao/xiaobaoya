#--coding:utf-8--
import requests

import itchat
city_name= input('请输入城市：')
wechat_name=input('请输入要发送的微信备注名：')
res= requests.get("http://wthrcdn.etouch.cn/weather_mini?city="+city_name)
r=res.json()
r1=r.get('data')
r2=r1.get('forecast')
#print(r.get('desc'))
f= open('tianqi.txt','w')
if r.get('desc') == 'OK':
    
        city =('城市：%s'%(r1.get('city')))
        Tday=('日期：%s'%(r2[0].get('date')))
        gan=('感冒：%s'%(r1.get('ganmao')))
        fx=('风向:%s'%(r2[0].get('fengxiang')))
        HT=(r2[0].get('high'))
        lw=(r2[0].get('low'))
        fl=("风力:%s"%(r2[0].get('fengli')))
        ty=('天气:%s'%(r2[0].get('type')))
    
        feg=('----------------------------------------------')
        ming=('日期：%s'%(r2[1].get('date')))
    
        f1=('风向:%s'%(r2[1].get('fengxiang')))
        h1=(r2[1].get('high'))
        l1=(r2[1].get('low'))
        fl1=("风力:%s"%(r2[1].get('fengli')))
        ty1=('天气:%s'%(r2[1].get('type')))
        feng1=('*************************************************************')
else:
    print('找不到该城市！')
itchat.auto_login(hotReload=True)
users=itchat.search_friends(wechat_name)[0]['UserName']
mess="%s\n%s\n%s\n%s\%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n"%(city,Tday,gan,fx,HT,lw,fl,ty,feg,ming,f1,h1,l1,fl1,ty1,feng1)
itchat.send(mess,toUserName=users)
print('发送成功，若没有即使收到请等待！')
