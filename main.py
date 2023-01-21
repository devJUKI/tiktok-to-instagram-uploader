from instagram_uploader import InstagramUploader
from tiktok_watermark_remover import TikTokWatermarkRemover
from facebook_api import FacebookAPI

instagram_account_id = 'XXXXXXXXXX'
caption = "XXXXXXXXXX"
share_to_feed = "true"
thumb_offset = 0

facebook_api = FacebookAPI()
facebook_access_token = facebook_api.get_access_token()

# Get TikTok video url without watermark
print('Getting TikTok video without watermark...')
tiktok_url = 'XXXXXXXXXX'
watermark_remover = TikTokWatermarkRemover()
video_url = watermark_remover.get_video_url(tiktok_url)

# Upload video to Instagram
print('Starting to upload reel to Instagram...')
ig_uploader = InstagramUploader(instagram_account_id, facebook_access_token)
ig_uploader.upload_reel(caption, share_to_feed, thumb_offset, video_url)

print('Done')
