import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)

        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getPassword().send_keys("12345")
        homePage.getCheckbox().click()
        homePage.getRadioBtn().click()

        self.selectDropDownByText(homePage.getGender(), getData["gender"])
        self.selectDropDownByIndex(homePage.getGender(), 0)

        homePage.clickSubmitBtn()
        message = homePage.alertSuccessMessage()
        homePage.validateMessage("Success", message)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
