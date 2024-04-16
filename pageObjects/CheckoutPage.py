from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitle = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    addBtn = (By.XPATH, "div/button")
    CheckoutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    successCheckoutBtn = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductTitles(self):
        # get the list of items and iterate to get Blackberry then click add to cart
        return self.driver.find_elements(*CheckOutPage.productTitle)

    def selectProduct(self, productList, productName):
        for product in productList:
            product_name = product.find_element(*CheckOutPage.productName).text
            if product_name == productName:
                product.find_element(*CheckOutPage.addBtn).click()

    def clickCheckoutItems(self):
        return self.driver.find_element(*CheckOutPage.CheckoutBtn).click()

    def clickCheckOutBtn(self):
        self.driver.find_element(*CheckOutPage.successCheckoutBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
