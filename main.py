import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Path to the Chrome executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Path to the user data directory
user_data_dir = r"C:\Users\Desmin\Desktop\VUE PROJECTS\mf-automator\chrome_user_data"

# Start Chrome with remote debugging using subprocess
subprocess.Popen([chrome_path, '--remote-debugging-port=9222', f'--user-data-dir={user_data_dir}'])

# Wait for Chrome to start
time.sleep(5)  # Adjust this as needed

# Set Chrome options to attach to the running instance
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# Initialize the WebDriver and attach to the running instance of Chrome
driver = webdriver.Chrome(options=chrome_options)

# Your automation script continues from here...
driver.get("http://chrisdalbano.com")
time.sleep(5)  # Wait for the page to load

# Find and interact with elements as needed
# ...

# Use driver.quit() or driver.close() as needed
#driver.close() to close the script
driver.close()