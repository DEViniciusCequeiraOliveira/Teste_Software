import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)


def get_path_with_file_name(filename: str) -> str:
    return os.getcwd() + filename


driver.get(get_path_with_file_name("/Login.html"))

element_search_field = driver.find_element(By.ID, "email")
element_search_field.send_keys("test@example.com")
element_password_field = driver.find_element(By.ID, "password")
element_password_field.send_keys("123456789")
element_button_submit_search = driver.find_element(By.ID, "signin")
element_button_submit_search.click()
