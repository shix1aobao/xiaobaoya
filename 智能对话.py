import requests as rs
import json
import os
import time

global userid

class usid:
    def __init__(self):
        self.uid = str(int(time.time()))
userid = usid()

def talk(content):       
    s = rs.session()
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key": "e76a82daaf71493bb303f1ebae3f77ad",
          "info": content ,
          "userid": userid.uid }
    data = json.dumps(da)
    r = s.post(url, data=data)
    j = eval(r.text)
    code = j['code']
    try:
        if code == 100000:
            recontent = j['text']
        elif code == 200000:
            recontent = j['text']+j['url']
        elif code == 302000:
            recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
        elif code == 308000:
            recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
        else:
            recontent = '这货还没学会怎么回复这句话'
    except:
        recontent = '这货还没学会怎么回复这句话'
    return recontent

print ('''
  *********************************
/ / / /                     \ \ \ \ 
/ / /     欢迎光临毛毛的小屋    \ \ \ 
-------------------------------------
##      _____                      ##
##     |  |  |                     ##
##     |--+--|                     ## 
##     |__|__|          (=^_^=)    ##
##                                 ##
##                                 ##

PS: 《直接按回车退出》

''')

print ("毛毛： 主人，见到你好开心啊！")
while True:
    ask = input("你  ： ")
    if ask == "":
        break
    else:
        res = talk(ask)
        if res == '这货还没学会怎么回复这句话':
            print (res)
        else:
            print ("毛毛： " , res)
        #i= os.system('mshta vbscript:createobject("sapi.spvoice").speak("%s")(window.close)' % res)
