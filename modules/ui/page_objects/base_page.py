from selenium import webdriver
from selenium.webdriver.safari.service import Service


class BasePage:
    PATH = "/Users/apple/RiabkoQAAuto23/"
    DRIVER_NAME = "safaridriver"

    def __init__(self):
        self.driver = webdriver.Safari(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
