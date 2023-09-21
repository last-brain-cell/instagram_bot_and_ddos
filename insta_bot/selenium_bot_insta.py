from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def login(username: str, password: str, web_driver: webdriver):
    sleep(3)
    inputs = web_driver.find_elements(By.TAG_NAME, "input")
    inputs[-2].send_keys(username)
    inputs[-1].send_keys(password)
    sleep(2)
    buttons = web_driver.find_elements(By.XPATH, "//button[@type='submit']")
    buttons[0].click()
    sleep(3)
    web_driver.find_elements(By.XPATH, "//div[@role='button']")[-1].click()
    sleep(3)
    web_driver.find_element(By.XPATH, "//button[@class='_a9-- _a9_1']").click()


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


# message = "Yo I'm Naad's InstaBot"
# send_list = ['Aditya Shailesh Kulkarni', 'yasho', 'siddh', 'Saloni Jahagirdar', 'Priyanshu', 'Nicola', 'Vayuj Dhir', 'kingsexbomb', 'Harsh Choubey', 'Lala Arnav Vatsal', 'smolsanmeow']
# send_msg(send_list, msg=message, count=0)


if __name__ == "__main__":
    service = Service('chromedriver_mac_arm64')
    driver = webdriver.Chrome(service=service)
    driver.get('https://instagram.com')

    login('naad.daan__', 'wubbalubbadubdub', driver)
    send_msg([''], 'instabot test 1.0', count=1)

    while True:
        if KeyboardInterrupt:
            break
        else:
            driver.implicitly_wait(1)

    print("Logging out of account...")
    sleep(3)
    driver.quit()
