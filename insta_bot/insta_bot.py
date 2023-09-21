from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pdb
from random import randint


def guide():
    guide = '''
    This is a Selenium Based Instagram Bot that can do some cool stuff like:
    1. Login to Your Instagram Account.
    2. Send out Mass DMs to the people you follow.
    3. Watch reels
    4. 

    chrome_options.add_argument(<argument>) -> 
        None : Default Settings
        '--start-maximized' : Maximizes the browser window when it is launched.
        '--disable-infobars' : Disables the "Chrome is being controlled by automated software" infobar.
        '--disable-extensions' : Disables browser extensions.
        '--disable-popup-blocking' : Disables the popup blocker.
        '--incognito' : Launches the browser in incognito mode.
        '--user-agent' : Sets the user agent string for the browser.
        '--proxy-server' : Specifies a proxy server to use for the browser.

    -> Not sure if you can get banned by sending out too many messages or logging in too 
    many times but at least I haven't been banned yet.
    '''
    print(guide)


def login(username: str, password: str, driver: webdriver, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)  # maximum wait duration in case of network issues

    inputs = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    # pdb.set_trace()
    inputs[-2].send_keys(username)
    sleep(1)
    inputs[-1].send_keys(password)
    sleep(1)
    buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@type='submit']")))
    buttons[0].click()

    sleep(5)
    not_now1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='button']")))
    not_now1[-1].click()
    # driver.find_elements(By.XPATH, "//div[@role='button']")[-1].click()
    print('not_now1')
    sleep(1)
    not_now2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='_a9-- _a9_1']")))
    print('not_now2')
    not_now2[-1].click()


def send_msg(to: list, msg: str, count: int, driver: webdriver, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)
    dms = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@role='link']")))
    dms[5].click()
    sleep(2)
    chats = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='button']")))
    chats_list = []
    for chat in chats:
        chats_list.append(chat.text.split('\n')[0])
    sleep(2)
    chats_list.pop(0)
    chats_list.pop(0)

    initial_message: str = "Yo I'm Naad's InstaBot Pls Don't Report or else I'll get Banned, this is just a test"
    for receiver in to:
        try:
            send_index = chats_list.index(receiver) + 2

            sleep(1)
            chats[send_index].click()

            sleep(2)
            message_box = driver.find_element(By.XPATH, "//div[@role='textbox']")

            message_box.send_keys(initial_message)
            message_box.send_keys(Keys.ENTER)

            if count >= 0:
                for i in range(count):
                    sleep(2)
                    message_box.send_keys(msg)
                    message_box.send_keys(Keys.ENTER)
            else:
                while True:
                    sleep(2)
                    message_box.send_keys(msg)
                    message_box.send_keys(Keys.ENTER)

        except ValueError:
            continue


def goto_home(driver: webdriver, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)
    dms = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@role='link']")))
    dms[1].click()
    sleep(2)


def goto_reels(driver: webdriver, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)
    dms = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@role='link']")))
    dms[4].click()
    sleep(2)
    reels_stream(driver)


def reels_stream(driver: webdriver, max_wait = 30):
    wait = WebDriverWait(driver, max_wait)
    sleep(5)
    while True:
        sleep(3)
        # caption_element = driver.find_element(By.CSS_SELECTOR, "div.C4VMK span")
        # caption = caption_element.text
        # print("--"*100)
        # sleep(1)
        like = driver.find_elements(By.TAG_NAME, "button")
        # is_liked = randint(0,1)
        # if is_liked:
        #     like[0].click()
        sleep(1)
        like[0].send_keys(Keys.ARROW_DOWN)


def goto_explore(driver: webdriver, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)
    dms = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@role='link']")))
    dms[3].click()
    sleep(2)


def search(prompt: str, driver: webdriver, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)
    dms = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@role='link']")))
    dms[2].click()
    sleep(2)

    # search_input = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    # search_input[0].sendkeys(prompt)

#
    #
    #
    #
    search_input = driver.find_elements(By.TAG_NAME, "input")
    search_input[0].send_keys(prompt)


if __name__ == "__main__":
    guide()

    chromedriver_path = 'chromedriver_mac_arm64'
    chromedriver_options = Options()
    chromedriver_options.add_argument('--incognito')
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chromedriver_options)
    driver.get('https://instagram.com')

    username = 'naad.pvt'
    password = 'wubbalubbadubdub'

    login(username, password, driver=driver)

    to = ['Priyansh Goel']
    msg = 'instabot test'
    count = 5
    sleep(3)
    # send_msg(to, msg, count, driver=driver)
    # sleep(3)
    #
    goto_home(driver=driver)
    sleep(3)
    #
    # goto_explore(driver=driver)
    #  sleep(3)
    #
    goto_reels(driver=driver)
    sleep(3)
    # search("naad.daan__", driver)

    sleep(10)
    driver.quit()
