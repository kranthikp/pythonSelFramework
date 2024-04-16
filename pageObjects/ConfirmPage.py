from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    enterCountry = (By.ID, "country")
    selectCountryText = (By.LINK_TEXT, "India")
    iAgreeCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.XPATH, "//input[@value='Purchase']")
    successAlert = (By.CLASS_NAME, "alert-success")

    def enterCountryTextBox(self, input_text):
        return self.driver.find_element(*ConfirmPage.enterCountry).send_keys(input_text)

    def selectCountry(self, country):
        return self.driver.find_element(By.LINK_TEXT, country).click()

    def selectIAgreeCheckbox(self):
        return self.driver.find_element(*ConfirmPage.iAgreeCheckbox).click()

    def clickPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn).click()

    def getAlertText(self):
        return self.driver.find_element(*ConfirmPage.successAlert)

    def validateAlertText(self, expected_text, actual_text):
        assert expected_text in actual_text