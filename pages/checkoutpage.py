from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def complete(self, errors):
        self.driver.find_element(By.ID, "first-name").click()

        self.driver.find_element(By.ID, "first-name").send_keys("User")

        self.driver.find_element(By.ID, "last-name").click()

        self.driver.find_element(By.ID, "last-name").send_keys("User")

        self.driver.find_element(By.ID, "postal-code").click()

        self.driver.find_element(By.ID, "postal-code").send_keys("123")

        self.driver.find_element(By.ID, "continue").click()

        self.driver.find_element(By.ID, "finish").click()

        if not self.driver.find_element(By.TAG_NAME, "h2").text == "Thank you for your order!":
            errors.append("no order")
