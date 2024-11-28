from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "uname")
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.XPATH, "//input[@value='Login']")
        self.login_success = (By.XPATH,"//div[@class='main']/h2")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login_status(self):
        return self.driver.find_element(*self.login_success).text