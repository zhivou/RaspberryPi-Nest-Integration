import requests
import json
from driver_helper import DriverHelper
from selenium.webdriver.common.by import By
import time


#
# I guess thins pin is impossible to get automaticly,
# Selenium now grabbing a new pin code
#
class TokenHelper:

    nest_config = json.loads(open('nest_config.json').read())
    CLIENT_ID = nest_config['client_id']
    CLIENT_SECRET = nest_config['client_secret']
    AUTHORIZATION_URL = "https://home.nest.com/login/oauth2?client_id=" + CLIENT_ID + "&state=STATE"
    TOKEN_URL = "https://api.home.nest.com/oauth2/access_token"
    HEADERS = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    def __init__(self, bypass_aoth = 0):
        if bypass_aoth == 0:
            self.pin_code = self.get_pin(DriverHelper().chrome_headless())
            self.content = self.get_token()
            self.error_checker()
            self.json_writer()

    def get_pin(self,browser):

        #
        # Page Objects
        #
        email_xpath = "//input[@type='email']"
        password_xpath = "//input[@type='password']"
        submit_xpath = "//button[@type='submit']"
        allow_xpath = "//button[@data-test='button-oauth-submit']"
        pincode_xpath = "//div[@data-test='text-oauth-pincode']"

        #
        # Login Page:
        #
        browser.get(TokenHelper.AUTHORIZATION_URL)
        self.js_waiter(browser, email_xpath)
        browser.find_element(By.XPATH, email_xpath).send_keys(TokenHelper.nest_config['email'])
        browser.find_element(By.XPATH, password_xpath).send_keys(TokenHelper.nest_config['password'])
        browser.find_element(By.XPATH, submit_xpath).click()

        #
        # Allow page
        #
        self.js_waiter(browser, allow_xpath)

        #
        # Pin Code Page
        #
        browser.execute_script("arguments[0].click();", browser.find_element_by_xpath(allow_xpath))
        self.js_waiter(browser, pincode_xpath)

        return browser.find_element(By.XPATH, pincode_xpath).text

    def js_waiter(self, browser, xpath):
        count = 0
        print("Water initiated for " + xpath)
        while len(browser.find_elements(By.XPATH, xpath)) <= 0:
            time.sleep(1)
            count += 1
            print("Waiting " + str(count) + " sec")
            if count == 10:
                return

    def get_token(self):
        """ Gets the token from source link and saves it """
        payload = "client_id=" + TokenHelper.CLIENT_ID + "&client_secret=" + TokenHelper.CLIENT_SECRET + "&grant_type=authorization_code&code=" + self.pin_code
        response = requests.request("POST", TokenHelper.TOKEN_URL, data=payload, headers=TokenHelper.HEADERS)
        content = json.loads(response.content)
        print('Token has been created successfully and saved as json file.')
        return content

    def error_checker(self):
        try:
            error = self.content['error_description']
        except:
            error = None
        if error:
            raise Exception('Ops something went wrong: ' + self.content['error_description'])

    def json_writer(self):
        with open('token.json', 'w') as outfile:
            json.dump(self.content, outfile)