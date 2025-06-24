# Importamos nuestras clases personalizadas de Selenium
from TestingTools import SeleniumDriver, ShortHandSeleniumSelectors

# Importaciones adicionales de Selenium para interactuar con el DOM
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Librerías estándar para manejo de tiempo y archivos
import time
import os

# Variable global para numerar las capturas de pantalla
count = 1

# Función que toma una captura de pantalla y la guarda en la carpeta "screenshots"
def take_screenshot(driver, step_name):
    global count
    os.makedirs("screenshots", exist_ok=True)  # Crea la carpeta si no existe
    path = f"screenshots/{count}.{step_name}.png"  # Ruta con número y nombre del paso
    driver.save_screenshot(path)  # Captura la pantalla actual
    count += 1

# Función que genera un nombre de imagen con hora y nombre del paso (no se usa en este script actual)
def formatImageName(time_clock, name):
    return f"pruebas/{time_clock}-{name}.png"

# Función para registrar un evento de prueba, imprimir el log y tomar captura
def log(log_name, web_driver: WebDriver):
    time_test = time.ctime()  # Fecha y hora actual en formato legible
    time_clock = time_test.split(" ")[3]  # Extrae solo la hora

    take_screenshot(web_driver, log_name)  # Captura pantalla con nombre del paso
    print(f"{time_test} - {log_name}")     # Imprime en consola el log con la hora

# Función principal que automatiza la navegación en MercadoLibre
def main():
    url = "https://www.mercadolibre.com/"  # URL inicial
    driver = SeleniumDriver(url)           # Se crea instancia del navegador con esa URL
    driver.connect_webdriver()             # Se abre el navegador y se navega a la URL

    web_driver = driver.web_driver()       # Se obtiene el WebDriver
    short = ShortHandSeleniumSelectors(web_driver)  # Se instancian los selectores simplificados

    log("Inicio ejecución de la prueba", web_driver)  # Log inicial

    short.selectById("MX", True)  # Selección de país México (clic)
    log("Búsqueda país", web_driver)

    short.selectById("cb1-edit").send_keys("playstation 5")  # Escribe en el campo de búsqueda
    log("Se agrega parametro de búsqueda playstation 5", web_driver)

    time.sleep(2)  # Espera para carga de la página

    short.selectByClass("nav-search-btn", True)  # Clic en botón de búsqueda
    log("Se le da click a la búsqueda", web_driver)

    # Aceptación de cookies o términos, si se muestra el aviso
    short.selectByElement("button", "data-testid", "action:understood-button", True)
    log("Aceptación de términos y condiciones", web_driver)

    time.sleep(2)

    # Aplicar filtro de productos "Nuevos"
    short.selectBy("span", "class", "ui-search-filter-name", "Nuevo", True)
    log("Se le da click al filtro Nuevo", web_driver)

    # Aplicar filtro de ubicación: CDMX
    short.selectBy("span", "class", "ui-search-filter-name", "Distrito Federal", True)
    log("Se le da click al filtro CDMX", web_driver)

    # Despliega el menú de ordenamiento
    elementDropDown = short.selectByElement("div", "class", "andes-dropdown__standalone-arrow")
    short.clickDOMElement(elementDropDown)  # Clic en la flecha del desplegable
    log("Se despliega el listado del filtro", web_driver)

    time.sleep(2)

    # Selecciona la opción "Mayor precio" del menú de ordenamiento
    dropDownGrather = short.selectBy("span", "class", "andes-list__item-primary", "Mayor precio", True)
    short.clickDOMElement(dropDownGrather)  # Asegura que se hizo clic
    log("Se organizan los productos de mayor a menor", web_driver)

    # Recupera los primeros 5 productos listados
    elementsList = short.selectManyElementsByClass("ui-search-layout__item")
    elementsList = elementsList[:5]  # Limita a 5 elementos

    # Itera sobre los elementos para extraer nombre y precio
    for element in elementsList:
        title = element.find_element(By.CLASS_NAME, "poly-component__title-wrapper").text
        price = element.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text

        print(f"*** El producto es: {title} y el precio es {price}")  # Muestra resultados en consola

    # Cierra el navegador al finalizar la prueba
    driver.desconnectedWebDriver()

# Ejecuta la función principal solo si se corre el archivo directamente
if __name__ == "__main__":
    main()
