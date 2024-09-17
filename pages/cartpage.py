from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def confirm_cart(self, errors):
        if self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack":
            self.driver.find_element(By.ID, "checkout").click()
        else:
            errors.append("no element")
