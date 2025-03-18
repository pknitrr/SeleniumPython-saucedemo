import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\pksin\\PycharmProjects\\SeleniumPythonProjects\\saucedemo\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def get_login_page_url():
        url = config.get('login info','login_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('login info','username_value')
        return username

    # @staticmethod
    # def get_username_XPATH():
    #     username_value = config.get('login info','username_XPATH')
    #     return username_value

    @staticmethod
    def get_password():
        password = config.get('login info','password_value')
        return password

    # @staticmethod
    # def get_password_XPATH():
    #     password_value = config.get('login','password_XPATH')
    #     return password_value

    @staticmethod
    def get_invalid_username():
        invalid_username_value = config.get('login info','invalid_username_value')
        return invalid_username_value

    # @staticmethod
    # def get_login_button_XPATH():
    #     login_button = config.get('login info', 'login_button_XPATH')
    #     return login_button
