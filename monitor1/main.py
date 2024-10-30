import time
import browser_automation

karatu_browser = browser_automation.BrowserAutomation()
kumakou_browser = browser_automation.BrowserAutomation()

if __name__ == "__main__":
    # ログイン画面へ遷移
    karatu_browser.login()
    # 該当ページへ遷移
    time.sleep(3)
    karatu_browser.navigate()
    # 該当ページを表示
    karatu_browser.click_button_with_text(text="唐津砕石")

    # ログイン画面へ遷移
    kumakou_browser.login()
    # 該当ページへ遷移
    time.sleep(3)
    kumakou_browser.navigate()
    # 該当ページを表示
    kumakou_browser.click_button_with_text(text="熊礦石材")



