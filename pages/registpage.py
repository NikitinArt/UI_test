from selenium.webdriver.common.by import By


class RegistPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.saucedemo.com/')

    def auth(self):
        self.driver.find_element(By.ID, "user-name").click()

        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")

        self.driver.find_element(By.ID, "password").click()

        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")

        self.driver.find_element(By.ID, "login-button").click()
