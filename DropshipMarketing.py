from time import sleep
import requests


def status_of_upload(ig_container_id='', access_token=''):
    url = graph_url + ig_container_id
    param = {}
    param['access_token'] = access_token
    param['fields'] = 'status_code'
    response = requests.get(url, params=param)
    response = response.json()
    return response


def publish_container(creation_id='', access_token='', instagram_account_id=''):
    url = graph_url + instagram_account_id + '/media_publish'
    param = dict()
    param['access_token'] = access_token
    param['creation_id'] = creation_id
    response = requests.post(url, params=param)
    response = response.json()
    return response


graph_url = 'https://graph.facebook.com/v15.0/'
instagram_account_id = '17841456683250303'
access_token = 'EAAG3mMaKpxkBAOcfuSmS6h592ZBll5FJqJZCz2bl4vXE5ByCx7ZCyjlHhubL62qikk5jH9ba1ZA8c8PprS91qZBnTiO56RSZAJDQjUc0UoyKhG9PZCsCVZAF80y97OaET4cHGj9NwVG58v7N4Oprn1YkrCyLHZCDLHAnFXJ7kfkgzHQW8VHDZA500tIYaQdcW7QaIZBTVm5JPx3zZBPTkHtl1A3fl7N55ZBoBMvBuBTfiXtOr39RqjieXxLQ2'
caption = "HOW GOOD DOES THIS LOOK? 🔥 LINK IN BIO 🎁 #musthaves #flame #diffuser #fire #gift #giftideas #decoration #air #humidifier #Relaxation #ComfortLiving #AirQuality #HomeImprovement #HealthyLiving"
media_type = "REELS"
share_to_feed = "true"
thumb_offset = 0
video_url = "https://cdn.snaptik.app/v2/?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJodHRwczovL2FwaTE2LW5vcm1hbC1jLXVzZWFzdDFhLnRpa3Rva3YuY29tL2F3ZW1lL3YxL3BsYXkvP3ZpZGVvX2lkPXYxMjA0NGdkMDAwMGM5OTJuYXJjNzd1MWYyMTg3b2JnJmxpbmU9MCZpc19wbGF5X3VybD0xJnNvdXJjZT1QYWNrU291cmNlRW51bV9BV0VNRV9ERVRBSUwmZmlsZV9pZD0wYzE1N2U1ZTI5MjI0NWI5YWQ3ZTM0N2U1ZmVjNzc4NCIsImZpbGVuYW1lIjoiU25hcHRpay5hcHBfNzA4NDc3NjM1NjczNDg4MTA3MC5tcDQiLCJleHAiOjE2NzM3NDY1MzV9.tPG8xSyhNL50yXinaHnZbzG_DPTVUtbvms3iLRJl-V8&dl=1"

url = graph_url + instagram_account_id + '/media'
param = dict()
param['access_token'] = access_token
param['caption'] = caption
param['media_type'] = media_type
param['share_to_feed'] = share_to_feed
param['thumb_offset'] = thumb_offset
param['video_url'] = video_url
response = requests.post(url, params=param)

print("\n 1st response", response.content)
response = response.json()

print("Uploading reel...")
status = status_of_upload(response['id'], access_token)
print(status)
while (status['status_code'] == 'IN_PROGRESS'):
    sleep(5)
    status = status_of_upload(response['id'], access_token)
    print(status)

print("Publishing reel...")
media_id = publish_container(status['id'], access_token, instagram_account_id)
print(media_id)
