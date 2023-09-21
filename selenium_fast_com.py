from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Path to the ChromeDriver executable
chrome_driver_path = "insta_bot/chromedriver_mac_arm64"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://fast.com")

wait = WebDriverWait(driver, 60)  # Wait for a maximum of 60 seconds
speed_container = wait.until(EC.visibility_of_element_located((By.XPATH, "div[@class='speed-results-container succeeded']")))

# Get the internet speed value
speed = speed_container.get_attribute("textContent")

print("Internet speed:", speed)

# Quit the browser
driver.quit()
