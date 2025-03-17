from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    login_page_url = "https://www.saucedemo.com/"
    username = "//input[@id ='user-name']"
    password = "//input[@id ='password']"
    login_button = "//input[@id ='login-button']"

    def __init__(self,driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.get(self.login_page_url)

    def enter_username(self, username):
        self.driver.find_element(By.XPATH,self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.password).send_keys(password)

    def click(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

