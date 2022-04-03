# !/usr/bin/python
# -*- coding: utf-8 -*-
#-*-coding:gb2312-*-
import time
# import imp
import sys
import json
import os
import requests
import datetime

with open('config.json') as config_json:
    config_data = json.load(config_json)
    
server_url=''
api_type=''
for p in config_data['server']:
    if p['is_active'] == True:        
        server_url=p['server_url']
        api_type=p['api_type']

smh_url =''
smh_token1 =''
smh_token2 =''
smh_name=''
for p in config_data['smh_skill']:
    if p['is_active'] == True:        
        smh_url=p['smh_url']
        smh_token1=p['smh_token1']
        smh_token2=p['smh_token2']
        smh_name=p['smh_name']

def server_controll(data):
    answer_text=''
    answer_link =''
    use_link =False
    data = data.lower()
    if api_type=='REST':
        #HTTP Request
        #Header Parameters
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        # Body Parameters                        
        payload = {'data': data, 'smh_url':smh_url, 'smh_token1': smh_token1, 'smh_token2': smh_token2,'smh_name':smh_name}
        # print(str(json.dumps(payload)))
        # Get response from Server  
        try:
            response = requests.post(server_url, headers=headers, data= json.dumps(payload))
            # print(str(response.json()))
            payload = response.json()
            answer_text=payload['answer_text']
            answer_link =payload['answer_link']
            use_link =payload['use_link']
        except:
            answer_text='Lỗi kết nối tới máy chủ'
    return answer_text, answer_link, use_link 

if __name__ == '__main__':

    server_controll('Bây giờ là mấy giờ')