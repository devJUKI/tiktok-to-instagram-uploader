from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TikTokWatermarkRemover:
    snaptik_url = 'https://snaptik.app/en'

    def get_video_url(self, tiktok_url):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--headless")
        options.add_argument("--incognito")

        driver = webdriver.Chrome(options=options)
        driver.get(self.snaptik_url)

        driver.implicitly_wait(5)

        url_input = driver.find_element(By.ID, 'url')
        url_input.send_keys(tiktok_url)

        submit_button = driver.find_element(
            By.CLASS_NAME, 'hero-input-right').find_element(By.TAG_NAME, 'button')
        submit_button.click()

        download_button = driver.find_element(
            By.CLASS_NAME, 'down-right').find_element(By.TAG_NAME, 'a')
        url = download_button.get_attribute('href')

        driver.quit()

        return url
