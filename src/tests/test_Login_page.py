import pytest
import time
from selenium import webdriver
from src.POM.LoginPage import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()
user_name = os.getenv("user_name")
user_pwd = os.getenv("user_pwd")
url = os.getenv("user_url")


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_login(setup):
    login_page = LoginPage(setup)
    login_page.open_page(url)
    time.sleep(1)
    login_page.enter_username(user_name)
    time.sleep(1)
    login_page.enter_password(user_pwd)
    time.sleep(1)
    login_page.click_login()
    time.sleep(1)
    login_status_txt = login_page.login_status()
    print("Login_status_txt:\t", login_status_txt)
    assert "Login Successful" in login_status_txt, "Login is failed"
