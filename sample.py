# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    food = "トマト"

    # ドライバーの立ち上げ
    driver = webdriver.Chrome()

    # googleにアクセス
    driver.get("http://google.com/")
    driver.find_element(By.NAME, "q").send_keys(food)
    driver.implicitly_wait(30)  # ブラウザでページの表示が終わるまで待つ機能(秒)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    # ⌘を押しながらNAMEをクリック
    time.sleep(1)

    driver.close()


if __name__ == '__main__':
    main()
