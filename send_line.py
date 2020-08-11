#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,requests
from datetime import datetime

class SendLine():
  token = os.environ['LINE_ACCESS_TOKEN']
 
  def send(self,message):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    payload = {'message': message + str(now)}  # 送信メッセージ
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + self.token}
    res = requests.post(url, data=payload, headers=headers)  # LINE NotifyへPOST
