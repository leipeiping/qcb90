import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
#提现和充值
import requests
def log_andreg_(url,data,method='post'):
   header = {"X-Lemonban-Media-Type": 'lemonban.v2'}
   if method=='get':
       result=requests.get(url,json=data,headers=header)
   else:
       result = requests.post(url, json=data, headers=header)
   print(result.json())
   return result.json()
log_url='http://120.78.128.25:8766/futureloan/member/login'
log_data={'mobile_phone':'13999885520','pwd':'123456999'}
reg_url='http://120.78.128.25:8766/futureloan/member/register'
reg_data={'mobile_phone':'13999885520','pwd':'123456999'}
response=log_andreg_(log_url,log_data)
log_andreg_(reg_url,reg_data)
#充值
def recharge(url,data,method,header):
   if method=='get':
       result_2=requests.get(url,json=data,headers=header)
   else:
       result_2 = requests.post(url, json=data, headers=header)
   print("充值的请求结果是：{}".format(response))
token=response['data']['token_info']['token']
header_2 = {"X-Lemonban-Media-Type": 'lemonban.v2', 'Authorization': 'Bearer '+token}
rec_url = 'http://120.78.128.25:8766/futureloan/member/recharge'
rec_data = {'member_id': '200013', 'amount': '3000'}
recharge(rec_url,rec_data,'post',header_2)
#提现
def withdraw(url,data,method,header):
   if method=='get':
       result_3=requests.get(url,json=data,headers=header)
   else:
       result_3 = requests.post(url, json=data, headers=header)
   print("提现结果是：{}".format(response))
token=response['data']['token_info']['token']
header_3 = {"X-Lemonban-Media-Type": 'lemonban.v2', 'Authorization': 'Bearer '+token}
wit_url = 'http://120.78.128.25:8766/futureloan/member/withdraw'
wit_data = {'member_id': '200013', 'amount': '1000'}
withdraw
