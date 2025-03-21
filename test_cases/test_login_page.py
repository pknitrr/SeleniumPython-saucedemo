import os
import pytest
from selenium import webdriver
from utilities.read_properties import ReadConfig
from selenium.webdriver.common.by import By
from base_pages.login_page import LoginPage
from utilities.custom_logger import LogMaker

class TestLoginPage:

    username = "//input[@id ='user-name']"
    password= "//input[@id ='password']"
    login_button = "//input[@id ='login-button']"
    login_page_url = ReadConfig.get_login_page_url()
    username_value = ReadConfig.get_username()
    password_value = ReadConfig.get_password()
    invalid_username_value = ReadConfig.get_invalid_username()
    #use logger
    logger  = LogMaker.log_generate()

    # username = ReadConfig.get_username()
    # password = ReadConfig.get_password()
    # invalid_username = ReadConfig.get_invalid_username()
    # login_button = ReadConfig.get_login_button()


    def test_title(self,setup):
        self.logger.info("************************** TC01: test_title started **************************")
        self.driver = setup
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page(self.login_page_url)
        act_title =self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            assert True
            self.obj_LoginPage.take_screenshot("test_title")
            self.logger.info("************************** TC01: test_title completed successfully **************************")

            self.driver.close()
        else:
            self.obj_LoginPage.take_screenshot("test_title")
            self.logger.info("************************** TC01: test_title Failed **************************")

            self.driver.close()
            assert False


    def test_validLogin(self,setup):
        self.logger.info("************************** TC02: test_validLogin started **************************")
        self.driver = setup
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page(self.login_page_url)
        self.obj_LoginPage.enter_username(self.username,self.username_value)
        self.obj_LoginPage.enter_password(self.password,self.password_value)
        self.obj_LoginPage.click_login(self.login_button)
        secondary_title = "//span[@class='title']"
        act_title = self.driver.find_element(By.XPATH,secondary_title).text
        exp_title = "Products"
        if act_title == exp_title:
            assert True
            self.obj_LoginPage.take_screenshot("test_validLogin")
            self.logger.info(
                "************************** TC02: test_validLogin completed successfully **************************")
            #self.driver.save_screenshot(".\\screenshots\\test_validLogin.png")
            self.driver.close()
        else:
            self.obj_LoginPage.take_screenshot("test_validLogin")
            self.logger.info("************************** TC02: test_validLogin Failed **************************")
            self.driver.close()
            assert False


    def testInvalidLogin(self,setup):
        self.logger.info("************************** TC03: testInvalidLogin started **************************")
        self.driver = setup
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page(self.login_page_url)
        self.obj_LoginPage.enter_username(self.username,self.invalid_username_value)
        self.obj_LoginPage.enter_password(self.password,self.password_value)
        self.obj_LoginPage.click_login(self.login_button)
        error_msg = self.driver.find_element(By.XPATH,"//h3[@data-test='error']").text
        print("error_msg",error_msg)
        if error_msg.__contains__("Username and password do not match "):
            assert True
            self.obj_LoginPage.take_screenshot("testInvalidLogin")
            self.logger.info("************************** TC03: testInvalidLogin completed successfully **************************")
            self.driver.close()
        else:
            self.obj_LoginPage.take_screenshot("testInvalidLogin")
            self.logger.info("************************** TC03: testInvalidLogin Failed **************************")
            self.driver.close()
            assert False







