from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radioBtn = (By.CSS_SELECTOR, "#inlineRadio1")
    genderDropDown = (By.ID, "exampleFormControlSelect1")
    submitBtn = (By.XPATH, "//input[@type='submit']")
    alertMessage = (By.CLASS_NAME, "alert-success")
    def clickShopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckOutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getRadioBtn(self):
        return self.driver.find_element(*HomePage.radioBtn)

    def getGender(self):
        return self.driver.find_element(*HomePage.genderDropDown)

    def clickSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitBtn).click()

    def alertSuccessMessage(self):
        return self.driver.find_element(*HomePage.alertMessage).text

    def validateMessage(self, expected_text, actual_text):
        assert expected_text in actual_text

