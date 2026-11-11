from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
# Open the website
url = "https://www.accuweather.com/en/pk/karachi/261158/weather-forecast/261158"
driver.get(url)

# Give the page some time to load
time.sleep(5)

# Use your XPath to locate the target element
try:
    air_quality_block = driver.find_element(By.XPATH
    , "/html/body/div/div[7]/div[1]/div[1]/a[1]/div[2]/div[2]/div[4]")
    label = air_quality_block.find_element(By.CLASS_NAME, "label").text.strip()
    value = air_quality_block.find_element(By.CLASS_NAME, "value").text.strip()
    print(f"{label}: {value}")
except Exception as e:
    print("Error extracting Air Quality:", e)

# Close the browser
driver.quit()
