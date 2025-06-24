# Importaciones necesarias para configurar y manejar el navegador Chrome con Selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

# Librería estándar para pausas
import time

# Tipado de Selenium para el navegador y elementos web
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

# Mecanismos de localización de elementos y condiciones esperadas
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

# Permite simular acciones complejas del usuario (clics, arrastres, etc.)
from selenium.webdriver.common.action_chains import ActionChains

# Clase para controlar la instancia de Selenium WebDriver
class SeleniumDriver:
    def __init__(self, url):
        self.url = url                  # URL a la que se desea navegar
        self.__web_driver = None       # WebDriver privado que será inicializado

    # Método para conectar e iniciar el navegador
    def connect_webdriver(self):
        service = Service(ChromeDriverManager().install())  # Instala y configura automáticamente el ChromeDriver
        options = ChromeOptions()                           # Opciones del navegador
        options.add_argument("--window-size=1920,1000")     # Tamaño de la ventana del navegador
        driver = Chrome(service=service, options=options)   # Inicializa el navegador
        driver.get(self.url)                                # Navega a la URL especificada
        self.__web_driver = driver                          # Guarda el driver en la instancia
        return True

    # Método para cerrar el navegador con un pequeño retraso
    def desconnectedWebDriver(self):
        time.sleep(5)                 # Espera para poder ver el resultado final antes de cerrar
        self.__web_driver.quit()     # Cierra la instancia del navegador

    # Método público para obtener el WebDriver actual
    def web_driver(self):
        return self.__web_driver


# Clase con métodos simplificados para encontrar y manipular elementos web
class ShortHandSeleniumSelectors:
    def __init__(self, web_driver: WebDriver):
        self.__web_driver = web_driver  # Almacena el WebDriver activo para usarlo en los métodos

    # Encuentra un elemento por ID, y hace clic si se indica
    def selectById(self, name_id: str, click: bool = False):
        element = self.__web_driver.find_element(By.ID, name_id)
        if click:
            element.click()
        return element

    # Encuentra un elemento por clase, y hace clic si se indica
    def selectByClass(self, name_class: str, click: bool = False):
        element = self.__web_driver.find_element(By.CLASS_NAME, name_class)
        if click:
            element.click()
        return element

    # Encuentra un elemento usando un tag y una propiedad personalizada (usando XPath)
    def selectByElement(self, tag, name_propertie, value_propertie, click: bool = False):
        xpath = f"//{tag}[@{name_propertie}='{value_propertie}']"
        element = self.__web_driver.find_element(By.XPATH, xpath)
        if click:
            element.click()
        return element

    # Encuentra un elemento por tag, propiedad, valor y texto visible exacto
    def selectBy(self, tag, name_property, value_propertie, literal_text, click: bool = False):
        xpath = f"//{tag}[@{name_property}='{value_propertie}' and normalize-space(text())='{literal_text}']"
        element = self.__web_driver.find_element(By.XPATH, xpath)
        if click:
            element.click()
        return element

    # Realiza un clic simulado en un elemento usando ActionChains (para mayor compatibilidad)
    def clickDOMElement(self, element: WebElement):
        action = ActionChains(self.__web_driver)
        action.click(element).perform()

    # Retorna una lista de todos los elementos encontrados con la clase especificada
    def selectManyElementsByClass(self, name_class):
        return self.__web_driver.find_elements(By.CLASS_NAME, name_class)
