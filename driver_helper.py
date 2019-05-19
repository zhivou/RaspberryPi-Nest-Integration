from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverHelper:

    def chrome_headless(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path='/Users/dskrylev/.rvm/gems/ruby-2.4.2/bin/chromedriver', chrome_options=chrome_options)
        return driver