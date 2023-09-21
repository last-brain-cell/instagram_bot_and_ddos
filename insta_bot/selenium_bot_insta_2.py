import selenium.common
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import streamlit as st
from time import sleep


def guide():
    guide = '''
    This is a Selenium Based Instagram Bot that can do some cool stuff like:
    1. Login to Your Instagram Account.
    2. Send out Mass DMs to the people you follow.
    3. 
    
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


def login(username: str, password: str, max_wait: int = 30):
    wait = WebDriverWait(driver, max_wait)  # maximum wait duration in case of network issues

    inputs = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    inputs[-2].send_keys(username)
    inputs[-1].send_keys(password)

    buttons = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
    buttons[0].click()

    not_now1 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='button']")))
    not_now1[-1].click()

    not_now2 = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@class='_a9-- _a9_1']")))
    not_now2[-1].click()


def send_msg(to: list, msg: str, count: int):
    sleep(2)
    driver.find_elements(By.XPATH, "//a[@role='link']")[5].click()
    sleep(5)
    chats = driver.find_elements(By.XPATH, "//div[@role='button']")
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

            for i in range(count):
                sleep(2)
                message_box.send_keys(msg)
                message_box.send_keys(Keys.ENTER)

        except ValueError:
            continue


if __name__ == "__main__":
    try:
        st.title('Instagram Bot')
        service = Service('chromedriver_mac_arm64')

        choose_options = st.button("Choose Options")
        if choose_options:
            mode = st.radio("Choose Option?", [" ", '--headless', '--start-maximized', '--disable-infobars', '--disable-extensions', '--incognito', '--user-agent', '--proxy-server'], key='option')
            st.write(mode)

            launch = st.button("Launch Instagram")
            if launch:
                if mode != " ":
                    chrome_options = Options()
                    chrome_options.add_argument(mode)
                    driver = webdriver.Chrome(service=service, options=chrome_options)
                else:
                    driver = webdriver.Chrome(service=service)
                driver.get('https://instagram.com')

            login_button = st.button("Log In")
            if login_button:
                with st.form(key='login_form'):
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    submit_button = st.form_submit_button("Submit")

                    if submit_button:
                        login(username, password)

                        if st.button("Send a Message"):
                            msg = st.text_area("Enter Message")
                            to = st.text_input("Enter Receiver (in the form of lists):")
                            count = int(st.text_input("Enter Count", type=int))
                            send_msg(to, msg, count)




        # while True:
        #             if KeyboardInterrupt:
        #                 break
        #             else:
        #                 driver.implicitly_wait(1)
        #
        # print("Logging out of account...")
        # sleep(3)
        # driver.quit()

    except selenium.common.WebDriverException:
        pass
