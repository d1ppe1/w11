import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin:
    def test_successful_login(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()
            
            # Проверяем, что залогинились
            assert "inventory" in driver.current_url
        finally:
            driver.quit()

    def test_invalid_login(self):
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").send_keys("invalid_user")
            driver.find_element(By.ID, "password").send_keys("wrong_password")
            driver.find_element(By.ID, "login-button").click()
            
            # Проверяем сообщение об ошибке
            error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
            assert "do not match" in error_message.text
        finally:
            driver.quit()