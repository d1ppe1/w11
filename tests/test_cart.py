import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCart:
    def test_add_to_cart(self):
        driver = webdriver.Chrome()
        try:
            # Логинимся
            driver.get("https://www.saucedemo.com/")
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()
            
            # Добавляем товар в корзину
            driver.find_element(By.CLASS_NAME, "btn_inventory").click()
            
            # Проверяем, что товар добавлен
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
            assert cart_badge.text == "1"
        finally:
            driver.quit()