from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your Microsoft Edge WebDriver
driver_path = r"C:\Users\hp\Downloads\edgedriver_win64\msedgedriver.exe"

# Replace with the recipient's phone number in international format
recipient_number = "+916392313198"

# The message you want to send
message = "Hello! This is a message from Python."

# Initialize the WebDriver service for Microsoft Edge
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Wait for the user to scan the QR code
print("Please scan the QR code with your phone.")
time.sleep(30)  # Increased wait time for QR code scan

try:
    # Wait until the search box is visible and then interact with it
    search_box = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Search" and @role="textbox" and @contenteditable="true"]'))
    )
    print("Search box found, entering recipient number...")
    search_box.send_keys(recipient_number)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the chat to open
    time.sleep(5)
    
    # Find the message box and send the message
    message_box = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Type a message" and @role="textbox" and @contenteditable="true"]'))
    )
    print("Message box found, sending message...")
    message_box.send_keys(message)
    message_box.send_keys(Keys.RETURN)
    
    print("Message sent successfully!")
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait a bit before closing the browser
    time.sleep(5)
    # Close the browser
    driver.quit()
