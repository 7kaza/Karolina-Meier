#!/usr/bin/python3
from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

product = 'konsola nintendo switch'
postcode = '50-519'

class MediaMarktRegistration(unittest.TestCase):

    def setUp(self):
        print('Przygotowanie strony')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mediamarkt.pl/')

    def testWrongEmail(self):

        driver = self.driver

        print('Szukanie produktu')
        product_input = driver.find_element_by_id('query_querystring')
        product_input.send_keys(product)
        product_input.submit()

        print('Wybor z listy wlasciwego produktu i dodanie do koszyka')
        product_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//a[@data-offer-name="Konsola NINTENDO Switch + Joy-Con Niebiesko-czerwony v2 2019"][@class="js-product-name"]')))
        product_select.click()

        product_add = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//a[@class="js-pre-add-cart m-btn m-btn_primary m-btn_big"]')))
        product_add.click()

        print('Alert - kod pocztowy')
        postcode_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@id="enp_cart_postcode_type_postcode"]')))
        postcode_input.send_keys(postcode)

        zapisz_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[@id='js-postcode-submit']")))
        zapisz_btn.click()

        dalej_btn = driver.find_element_by_xpath("//a[@id='js-cartNext']")
        actions = ActionChains(driver)
        actions.move_to_element(dalej_btn)
        actions.perform()
        dalej_btn.click()


        time.sleep(5)

    #def tearDown(self):
        #self.driver.quit()
        time.sleep(50)
        #pass



if __name__ == '__main__':
    unittest.main(verbosity=2)
