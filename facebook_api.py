from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlencode, urlparse, parse_qs
import requests


class FacebookAPI:
    def get_access_token(self):
        oauth_code = self.get_auth_code()

        param = {
            'client_id': XXXXXXXXX,
            'redirect_uri': 'https://www.example.com/',
            'client_secret': 'XXXXXXXXX',
            'code': oauth_code,
        }

        access_token_url = 'https://graph.facebook.com/v15.0/oauth/access_token'

        request = requests.get(access_token_url, params=param)
        return request.json()['access_token']

    def get_auth_code(self):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)

        facebook_code_url = 'https://www.facebook.com/v15.0/dialog/oauth?'
        params = {
            'client_id': 483341770598169,
            'redirect_uri': 'https://www.example.com/',
            'scope': 'ads_management,business_management,instagram_basic,instagram_content_publish,pages_read_engagement'
        }
        oauth_url = facebook_code_url + urlencode(params)
        driver.get(oauth_url)

        try:
            WebDriverWait(driver, 60).until(
                lambda driver: driver.current_url.find('example.com/?code') != -1)
        except:
            print('You didn\'t login in time')
            driver.quit()
            return None
        else:
            redirected_url = driver.current_url

        driver.quit()

        parse_result = urlparse(redirected_url)
        dict_result = parse_qs(parse_result.query)

        return dict_result['code'][0]
