import os
import time

import pytest
from selenium import webdriver
from utilities.read_properties import ReadConfig
from selenium.webdriver.common.by import By
from base_pages.login_page import LoginPage
from utilities.custom_logger import LogMaker
import openpyxl
from utilities import excel_utils
class TestLoginPage:

    # username = "//input[@id ='user-name']"
    # password= "//input[@id ='password']"
    # login_button = "//input[@id ='login-button']"

    #use logger
    logger  = LogMaker.log_generate()
    #path = ".//test_data//login_data.xlsx"
    path = r"C:\Users\pksin\PycharmProjects\SeleniumPythonProjects\saucedemo\test_data\login_data.xlsx"
    status_list = []

    login_page_url = "https://www.saucedemo.com/"
    open_menu = "//*[@data-test='open-menu']"
    logout_button = "//*[@id='logout_sidebar_link']"

    def test_validLogin_data_driven(self,setup):
        self.logger.info("***************** TC02: test_validLogin_data_driven started ***************")
        self.driver = setup
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page(self.login_page_url)

        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print(self.rows)
        self.username = excel_utils.read_data(self.path, "Sheet1", 2, 1)
        print(self.username)
        self.password = excel_utils.read_data(self.path, "Sheet1", 2, 3)
        print(self.password)
        self.login_button = excel_utils.read_data(self.path, "Sheet1", 2, 5)

        for r in range(2, self.rows+1):

            self.username_value = excel_utils.read_data(self.path, "Sheet1", r, 2)
            self.password_value = excel_utils.read_data(self.path, "Sheet1", r, 4)
            self.exp_login = excel_utils.read_data(self.path, "Sheet1", r, 6)
            self.obj_LoginPage.enter_username(self.username, self.username_value)
            self.obj_LoginPage.enter_password(self.password,self.password_value)
            self.obj_LoginPage.click_login(self.login_button)

            time.sleep(1)
            secondary_title = "//span[@class='title']"
            act_title = self.driver.find_element(By.XPATH, secondary_title).text
            exp_title = "Products"

            if act_title == exp_title and self.exp_login == "Yes":
                self.logger.info("Test data is passed")
                self.status_list.append("Pass")
                self.obj_LoginPage.click_logout(self.open_menu,self.logout_button)
            elif act_title == exp_title and self.exp_login == "No":
                self.logger.info("Test data is Failed")
                self.status_list.append("Fail")
                self.obj_LoginPage.take_screenshot("test_validLogin")
                self.obj_LoginPage.click_logout(self.open_menu, self.logout_button)
            elif act_title != exp_title and self.exp_login == "Yes":
                self.logger.info("Test data is Failed")
                self.status_list.append("Fail")
                self.obj_LoginPage.take_screenshot("test_validLogin")
                self.obj_LoginPage.click_logout(self.open_menu, self.logout_button)
            elif act_title != exp_title and self.exp_login == "No":
                self.obj_LoginPage.take_screenshot("test_validLogin")
                self.logger.info("Test data is passed")
                self.status_list.append("Pass")
                self.obj_LoginPage.click_logout(self.open_menu, self.logout_button)

        print("status list is : ",self.status_list)

        if "Fail" in self.status_list:
            self.logger.info(
                "************** TC02: test_validLogin_data_driven Failed **************")
            assert False
        else:
            self.logger.info(
                "************** TC02: test_validLogin_data_driven completed successfully **************")
            assert True











