#!/usr/bin/env python
# coding: utf-8

import os
from twython import Twython

#twitterの認証情報を入力
CONSUMER_KEY = 'S1ecm8CIbNyRAJVECEnF7Uc5f'
CONSUMER_SECRET = 'N7HCVBWQdiSHUr0pKIIrKPioR5fvnkCRHiU2EidhUUjbk7AIeX'
ACCESS_KEY = '4080677840-93efyhMNEo9U1gxDm9Qj9Q2HJUk9SzAPbSoIRTa'
ACCESS_SECRET = 'TYgOIBVrSQpQxDpQANwpqeWfTcEP9KLF3xHpeAvWG1PCP'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#CPU温度を取得
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

#取得したCPU温度をツイート
# api.update_status(status= 'CPU温度は '+temp+' ℃です。')

space = '123'
api.update_status(status= space)
