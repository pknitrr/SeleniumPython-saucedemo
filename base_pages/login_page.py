import os

from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class LoginPage:


    login_page_url = "https://www.saucedemo.com/"
    username = "//input[@id ='user-name']"
    password = "//input[@id ='password']"
    login_button = "//input[@id ='login-button']"



    def __init__(self,driver):
        self.driver = driver

    def navigate_to_login_page(self,login_page_url):
        self.driver.get(login_page_url)

    def enter_username(self, username,username_value):
        self.driver.find_element(By.XPATH,username).send_keys(username_value)

    def enter_password(self, password, password_value):
        self.driver.find_element(By.XPATH, password).send_keys(password_value)

    def click_login(self, login_button):
        self.driver.find_element(By.XPATH, login_button).click()

    def click_logout(self,open_menu,logout_button):
        #self.driver.find_element(By.XPATH,open_menu).click()
        #actions = ActionChains(self.driver)
        #actions.move_to_element(open_menu).click().perform()
        self.driver.execute_script("arguments[0].click();", open_menu)
        #self.driver.execute_script("arguments[0].click();", logout_button)
        #self.driver.find_element(By.XPATH, logout_button).click()

    def take_screenshot(self,filename):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename_with_time = filename+f"screenshot_{timestamp}.png"
        print("os.getcwd()",os.getcwd())
        self.driver.save_screenshot(".\\screenshots\\"+filename_with_time)

