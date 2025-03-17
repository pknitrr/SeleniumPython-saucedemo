import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from base_pages.login_page import LoginPage


class TestLoginPage:

    username = "standard_user"
    password = "secret_sauce"


    def test_title(self):
        self.driver = webdriver.Edge()
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page()
        act_title =self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False


    def test_validLogin(self):
        self.driver = webdriver.Edge()
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page()
        self.obj_LoginPage.enter_username(self.username)
        self.obj_LoginPage.enter_password(self.password)
        self.obj_LoginPage.click()
        secondary_title = "//span[@class='title']"
        act_title = self.driver.find_element(By.XPATH,secondary_title).text
        exp_title = "Products"
        if act_title == exp_title:
            assert True
            #print(act_title)
            self.driver.close()
        else:
            self.driver.close()
            assert False



    def testInvalidLogin(self):
        self.driver = webdriver.Edge()
        self.obj_LoginPage = LoginPage(self.driver)
        self.obj_LoginPage.navigate_to_login_page()




