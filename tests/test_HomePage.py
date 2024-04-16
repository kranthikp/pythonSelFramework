import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):

        homePage = HomePage(self.driver)

        homePage.getName().send_keys("Panda")
        homePage.getEmail().send_keys("hello@gmail.com")
        homePage.getPassword().send_keys("12345")
        homePage.getCheckbox().click()
        homePage.getRadioBtn().click()

        self.selectDropDownByText(homePage.getGender(), "Female")
        self.selectDropDownByIndex(homePage.getGender(), 0)

        homePage.clickSubmitBtn()
        message = homePage.alertSuccessMessage()

        print(message)
        homePage.validateMessage("Success", message)