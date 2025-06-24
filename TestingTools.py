from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome  import ChromeDriverManager

import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait 
from selenium.webdriver.common.action_chains import ActionChains

class SeleniumDriver:
    def __init__(self, url):
        self.url = url
        self.__web_driver = None

    def connect_webdriver(self):
        service = Service(ChromeDriverManager().install())
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1000")
        driver = Chrome(service=service, options=options)
        driver.get(self.url)
        self.__web_driver = driver
        return True
    
    def desconnectedWebDriver(self):
        time.sleep(5)
        self.__web_driver.quit()
    
    def web_driver(self):
        return self.__web_driver
    

class ShortHandSeleniumSelectors:
    def __init__(self, web_driver: WebDriver):
        self.__web_driver = web_driver
    
    def selectById(self, name_id: str, click: bool = False):
        element = self.__web_driver.find_element(By.ID, name_id)
        if (click):
            element.click()
        return element

    def selectByClass(self, name_class: str, click: bool = False):
        element = self.__web_driver.find_element(By.CLASS_NAME, name_class)
        if (click):
            element.click()
        return element

    def selectByElement(self, tag, name_propertie, value_propertie, click: bool = False):
        element = self.__web_driver.find_element(By.XPATH, f"//{tag}[@{name_propertie}='{value_propertie}']")
        if (click):
            element.click()
        return element

    def selectBy(self, tag, name_property, value_propertie, literal_text, click: bool = False):
        xpath = f"//{tag}[@{name_property}='{value_propertie}' and normalize-space(text())='{literal_text}']"
        element = self.__web_driver.find_element(By.XPATH, xpath)
        if (click):
            element.click()
        return element
    
    def clickDOMElement(self, element: WebElement):
        action = ActionChains(self.__web_driver)
        action.click(element).perform()

    def selectManyElementsByClass(self, name_class):
        return self.__web_driver.find_elements(By.CLASS_NAME, name_class)
