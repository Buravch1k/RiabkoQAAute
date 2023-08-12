from selenium.webdriver.common.by import By
from modules.ui.page_objects.base_page import BasePage


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self):
        super().__init__()

    def try_login(self, username, password):
        self.driver.get(SignInPage.URL)

        self.driver.find_element(By.ID, "login_field").send_keys(username)

        self.driver.find_element(By.ID, "password").send_keys(password)

        self.driver.find_element(By.NAME, "commit").click()

    def check_title(self, title_expected):
        return self.driver.title == title_expected
