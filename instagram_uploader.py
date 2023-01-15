from time import sleep
import requests


class InstagramUploader:
    graph_url = 'https://graph.facebook.com/v15.0/'

    def __init__(self, instagram_account_id, access_token):
        self.instagram_account_id = instagram_account_id
        self.access_token = access_token

    def upload_reel(self, caption, share_to_feed, thumb_offset, video_url):
        print('Creating container...')
        response = self.create_container(
            caption, share_to_feed, thumb_offset, video_url)

        print('Uploading container...')
        status = self.get_upload_status(response['id'])
        print(status)
        while (status['status_code'] == 'IN_PROGRESS'):
            sleep(5)
            status = self.get_upload_status(response['id'])
            print(status)

        print('Container published!')
        media_id = self.publish_container(status['id'])

        quota_usage = self.get_quota_usage()
        uploads_left_today = 25 - quota_usage
        print('You have published', quota_usage,
              'reels today.', uploads_left_today, 'left.')

        return media_id

    def create_container(self, caption, share_to_feed, thumb_offset, video_url):
        url = self.graph_url + self.instagram_account_id + '/media'

        param = dict()
        param['access_token'] = self.access_token
        param['caption'] = caption
        param['media_type'] = "REELS"
        param['share_to_feed'] = share_to_feed
        param['thumb_offset'] = thumb_offset
        param['video_url'] = video_url

        response = requests.post(url, params=param)
        response = response.json()
        return response

    def publish_container(self, creation_id):
        url = self.graph_url + self.instagram_account_id + '/media_publish'

        param = dict()
        param['access_token'] = self.access_token
        param['creation_id'] = creation_id

        response = requests.post(url, params=param)
        response = response.json()
        return response

    def get_upload_status(self, ig_container_id=''):
        url = self.graph_url + ig_container_id

        param = {}
        param['access_token'] = self.access_token
        param['fields'] = 'status_code'

        response = requests.get(url, params=param)
        response = response.json()
        return response

    def get_quota_usage(self):
        url = self.graph_url + self.instagram_account_id + '/content_publishing_limit'

        param = {}
        param['access_token'] = self.access_token

        response = requests.get(url, params=param)
        response = response.json()
        return response['data'][0]['quota_usage']
