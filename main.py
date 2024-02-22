from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pyautogui

# Create a Chrome Options object
chrome_options = Options()

# Specify a custom user data directory (change the path as per your preference)
user_data_dir = (
    "C:\\Users\\Desmin\\Desktop\\VUE PROJECTS\\mf-automator\\chrome_user_data"
)

# Add the user data directory to Chrome options
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# Path to the ChromeDriver executable
chromedriver_path = "C:\\Users\\Desmin\\Desktop\\VUE PROJECTS\\mf-automator\\chromedriver.exe"

# Create a Service object passing the path to chromedriver
service = Service(executable_path=chromedriver_path)

# Initialize the Chrome WebDriver with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a new tab in an existing Chrome window
driver.execute_script("window.open('');")
time.sleep(2)  # Wait for the new tab to open

# Switch to the new tab, which is the second tab (index 1 as it's 0-based)
driver.switch_to.window(driver.window_handles[1])

# Navigate to a specific URL
driver.get("http://chrisdalbano.com")

# Wait for the page to load
time.sleep(5)  # Adjust timing based on your internet speed and page load time

# Look for a specific <div> element, focus field, and input text

button_div = driver.find_element(By.CSS_SELECTOR, "#app > div > section.p-4.md\:p-20.lg\:p-32 > button")
button_div.click()
time.sleep(5)

# Optionally, use PyAutoGUI for more advanced desktop interactions
# pyautogui.write('Your text here')
# pyautogui.press('enter')

# Search for a specific div element and click it
# Update the CSS selector for the specific div as per your requirements
specific_div = driver.find_element(By.CSS_SELECTOR, "#app > div > div.grid.grid-cols-1.sm\:grid-cols-2.lg\:grid-cols-4.gap-4.text-gray-900.px-2.sm\:px-4.md\:px-6.lg\:px-8.lg\:text-2xl.pb-8 > div:nth-child(1)")
specific_div.click()

# Remember to close the browser once done
driver.quit()
