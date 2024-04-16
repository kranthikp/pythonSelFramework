import pytest

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homePage = HomePage(self.driver)

        homePage.getName().send_keys(getData[0])
        homePage.getEmail().send_keys(getData[1])
        homePage.getPassword().send_keys("12345")
        homePage.getCheckbox().click()
        homePage.getRadioBtn().click()

        self.selectDropDownByText(homePage.getGender(), getData[2])
        self.selectDropDownByIndex(homePage.getGender(), 0)

        homePage.clickSubmitBtn()
        message = homePage.alertSuccessMessage()
        homePage.validateMessage("Success", message)

        self.driver.refresh()

    @pytest.fixture(params=[("Kranthi", "Panda", "Male"), ("Meera", "Panda", "Female")])
    def getData(self, request):
        return request.param
