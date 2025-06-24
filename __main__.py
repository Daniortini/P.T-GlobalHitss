from TestingTools import SeleniumDriver, ShortHandSeleniumSelectors
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import time
import os

count = 1

def take_screenshot(driver, step_name):
    global count
    os.makedirs("screenshots", exist_ok=True)
    path = f"screenshots/{count}.{step_name}.png"
    driver.save_screenshot(path)
    count += 1

def formatImageName(time_clock, name):
    return f"pruebas/{time_clock}-{name}.png"

def log(log_name, web_driver: WebDriver):
    time_test = time.ctime()
    time_clock = time_test.split(" ")[3]

    take_screenshot(web_driver, log_name)

    print(f"{time_test} - {log_name}")

def main():
    url = "https://www.mercadolibre.com/"
    driver = SeleniumDriver(url)
    driver.connect_webdriver()

    web_driver = driver.web_driver()
    short = ShortHandSeleniumSelectors(web_driver)

    log ("Inicio ejecución de la prueba", web_driver)

    short.selectById("MX", True)
    log("Búsqueda país", web_driver)

    short.selectById("cb1-edit").send_keys("playstation 5")
    log("Se agrega parametro de búsqueda playstation 5", web_driver)

    time.sleep(2)

    short.selectByClass("nav-search-btn", True)
    log("Se le da click a la búsqueda", web_driver)

    short.selectByElement("button", "data-testid", "action:understood-button", True)
    log("Aceptación de términos y condiciones", web_driver)

    time.sleep(2)

    short.selectBy("span", "class", "ui-search-filter-name", "Nuevo", True)
    log("Se le da click al filtro Nuevo", web_driver)

    short.selectBy("span", "class", "ui-search-filter-name", "Distrito Federal", True)
    log("Se le da click al filtro CDMX", web_driver)

    elementDropDown = short.selectByElement("div", "class", "andes-dropdown__standalone-arrow")
    short.clickDOMElement(elementDropDown)
    log("Se despliega el listado del filtro", web_driver)

    time.sleep(2)

    dropDownGrather = short.selectBy("span", "class", "andes-list__item-primary", "Mayor precio", True)
    short.clickDOMElement(dropDownGrather)
    log("Se organizan los productos de mayor a menor", web_driver)

    elementsList = short.selectManyElementsByClass("ui-search-layout__item")
    elementsList = elementsList[:5]

    for element in elementsList:
        title = element.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text
        price = element.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text

        print(f"*** El producto es: {title} y el precio es {price}")

    driver.desconnectedWebDriver()

if __name__ == "__main__":
    main()