# # noinspection PyUnresolvedReferences
# import time
#
# # noinspection PyUnresolvedReferences
# import chromedriver_binary
# # noinspection PyUnresolvedReferences
# from selenium import webdriver
# # noinspection PyUnresolvedReferences
# from selenium.webdriver.common.by import By
# # noinspection PyUnresolvedReferences
# from selenium.webdriver.common.keys import Keys
#
# URL = "http://cookpad.com"  # グローバル変数
# driver = webdriver.Chrome()
#
#
# def search_by_food(driver, food):
#     driver.get(f"{URL}")
#     driver.implicitly_wait(30)
#     driver.find_element(By.ID, "keyword").send_keys(food)
#     driver.find_element(By.ID, "submit_button").click()
#     driver.implicitly_wait(10)
#
#
# def get_recipes(driver):
#
#
#
# def main():
#     food = "トマト"
#     # driver.get("http://google.com/")
#     # driver.implicitly_wait(30)
#     # driver.close()
#
#     # withの方法(closeのつけ忘れ防止)
#     with webdriver.Chrome() as driver:
#         search_by_food(driver, food)
#         get_recipes(driver)
#
# if __name__ == '__main__':
#     main()


# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys

URL = "https://cookpad.com"


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # ヘッドレスモード
    # options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
    # options.add_argument("--enable-javascript")  # JS無効
    return options


def search_by_food(driver, food):
    driver.get(f"{URL}")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "keyword").send_keys(food)  # 検索にfoodの内容を入力
    driver.find_element(By.ID, "submit_button").click()  # 検索ボタンを押す
    time.sleep(10)


def get_recipes(driver):
    recipe_previews = driver.find_elements(By.CLASS_NAME, "recipe-preview")
    # print(recipe_previews)

    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_elements(By.CLASS_NAME, "recipe-title").text
        recipe_url = recipe_preview.find_elements(By.CLASS_NAME, "recipe-title").get_attribute("href")
        print(recipe_title, recipe_url)


def main():
    food = 'トマト'

    # 前の方法
    # driver = webdriver.Chrome()
    # driver.get("")
    # driver.implicitly_wait(10)
    # driver.close()

    # withの方法(close忘れ防止)
    with webdriver.Chrome(options=chromedriver_options()) as driver:
        search_by_food(driver, food)
        get_recipes(driver)


if __name__ == '__main__':
    main()
