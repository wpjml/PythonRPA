import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserAutomation:

    def __init__(self):
        self.login_url = "https://nsupport.nglobal.jp"
        self.LOGIN_ID = "NIWTESTSALES"
        self.PASSWORD = "654321"
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(self.login_url)

        # ログインidの入力
        time.sleep(2)
        login_id_element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div[2]/div/div/input')
        login_id_element.send_keys(self.LOGIN_ID)

        # パスワードの入力
        time.sleep(2)
        password_element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div[3]/div/div/input')
        password_element.send_keys(self.PASSWORD)

        # ログイン
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/form/div[4]/button')
        login_button.click()

    def navigate(self):
        time.sleep(3)
        # 機械データのボタンをクリック
        machine_data_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="main-content"]/div/div[1]/div[2]/div[5]/div/div/a'
        )
        machine_data_button.click()

        # ライブビューのボタンをクリック
        time.sleep(3)
        realtime_view_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="main-content"]/div[1]/div[1]/div/div/div[2]/div/a[1]/button'
        )
        realtime_view_button.click()

        # 一番下までスクロール
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def click_button_with_text(self, text):
        try:
            # ボタンがクリック可能になるまで待機
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{text}')]"))
            )
            # ボタンをクリック
            button.click()
        except Exception as e:
            print(f"'{text}' を含むボタンが見つかりませんでした。エラー: {e}")

        # 社名を隠す為にスクロール
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 135);")
        time.sleep(1)

    def close_browser(self):
        # ブラウザを閉じる
        if self.driver:
            self.driver.quit()

    def move_window_to_monitor_and_fullscreen(self):
        # 後ほど実装
        pass
