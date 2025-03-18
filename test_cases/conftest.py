import pytest
from pytest_metadata.plugin import metadata, metadata_key
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default ="edge",help ="Specify Browser from chrome, firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("unsupported Browser")
    return driver

# @pytest.fixture()
# def setup():
#     driver = webdriver.Edge()
#     return driver

#################### pytest html reports customization #########################
#hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'saucedemo'
    config.stash[metadata_key] ['Test Module Name'] = 'Login Tests'
    config.stash[metadata_key] ['Tester Name'] = 'Pushpendra Singh'

#hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins',None)

