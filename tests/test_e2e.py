import pytest

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        # login into homepage"
        homePage = HomePage(self.driver)
        # click Shop on Header to navigated to checkout page
        checkOutPage = homePage.clickShopItems()
        # get product details
        log.info("Getting all the product titles")
        productList = checkOutPage.getProductTitles()
        # select product
        checkOutPage.selectProduct(productList, "Blackberry")
        # click checkout items
        checkOutPage.clickCheckoutItems()
        # final click checkout button
        confirmPage = checkOutPage.clickCheckOutBtn()
        log.info("Entering the country name as Ind")
        # enter Text "ind"
        confirmPage.enterCountryTextBox("Ind")
        # verify India is present on dropdown list
        self.verifyLinkPresence("India")
        # select India from the list
        confirmPage.selectCountry("India")
        # select I Agree checkbox
        confirmPage.selectIAgreeCheckbox()
        # click Purchase button on Confirm Page
        confirmPage.clickPurchaseBtn()
        # get alert success text
        actual_message = confirmPage.getAlertText().text
        log.info("text received from app is "+actual_message)
        # assert the expected message with the actual message
        confirmPage.validateAlertText("Success! Thank you!", actual_message)


