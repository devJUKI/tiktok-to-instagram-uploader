from instagram_uploader import InstagramUploader
from tiktok_watermark_remover import TikTokWatermarkRemover

instagram_account_id = 'XXXXXXXXXX'
access_token = 'XXXXXXXXXX'
caption = "XXXXXXXXXX"
share_to_feed = "true"
thumb_offset = 0

# Get TikTok video url without watermark
tiktok_url = 'XXXXXXXXXX'
watermark_remover = TikTokWatermarkRemover()
video_url = watermark_remover.get_video_url(tiktok_url)

# Upload video to Instagram
ig_uploader = InstagramUploader(instagram_account_id, access_token)
ig_uploader.upload_reel(caption, share_to_feed, thumb_offset, video_url)

print('Done')
