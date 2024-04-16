import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("First Name is "+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])

        log.info("Last Name is " + getData["lastname"])
        homePage.getEmail().send_keys(getData["lastname"])

        homePage.getPassword().send_keys("12345")
        homePage.getCheckbox().click()
        homePage.getRadioBtn().click()

        log.info("Gender is " + getData["gender"])
        self.selectDropDownByText(homePage.getGender(), getData["gender"])
        self.selectDropDownByIndex(homePage.getGender(), 0)

        homePage.clickSubmitBtn()
        message = homePage.alertSuccessMessage()
        homePage.validateMessage("Success", message)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self, request):
        return request.param
