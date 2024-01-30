import pytest
import time
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


#LAS PRIMERAS 3 PRUEBAS SERAN POR SCRIPT SEPARADO CON NAVEGADORES DIFERENTES
#PRIMERA OPCION PARA QUITAR UNA VENTANA EMERGENTE EN CHROME ANTES DE EXPLORAR LA PAGINA WEB
@pytest.mark.notrun
#paso 1 Se entra a la url de la pagina web y quitamos la ventana emergente
def test_uno():
    driver = webdriver.Chrome()
    driver.get("https://www.equifax.com.sv/efx-app-web-portal-sv/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(2)

#En el paso 2 tenemos que quitar la ventana emergente que aparece antes de interactuar con la pagina web
    vemergente  = driver.find_element(By.XPATH, "//span[contains(@aria-hidden,'true')]").click()

#Este es el paso 3 validamos el titulo de la web luego de ya haber quitado la ventana emergente y listo queda limpia la pagina web para explorarla
    driver.get("https://www.equifax.com.sv/efx-app-web-portal-sv/")
    try:
        assert "Equifax - Portal" == driver.title
        print("Prueba exitosa: El titulo de la pagina es correcto")
    except AssertionError:
        print("Prueba fallida: El titulo de la pagina no es correcto")

    driver.quit()




#SEGUNDA OPCION PARA QUITAR UNA VENTANA EMERGENTE EN FIREFOX ANTES DE EXPLORAR LA PAGINA WEB
@pytest.mark.notrun
#paso 1 se entra en la url de la pagina web y quitamos la ventana emergente
def test_dos():
    driver = webdriver.Firefox()
    driver.get("https://www.equifax.com.sv/efx-app-web-portal-sv/")
    driver.maximize_window()
    driver.implicitly_wait(10)

#en el paso 2 tenemos que quitar la ventana emergente que aparece antes de interactuar con la pagina web
    vemergente2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[7]/div/div/div[1]/button/span"))
    )
    vemergente2.click()

#paso 3 donde validamos el titulo de la pagina web para poder explorarla luego de haber cerrado la ventana emergente
    driver.get("https://www.equifax.com.sv/efx-app-web-portal-sv/")
    try:
        assert "Equifax - Portal" == driver.title
        print("Prueba exitosa: El titulo de la pagina es correcto")
    except AssertionError:
        print("Prueba fallida: El titulo de la pagina no es correcto")
    driver.quit()



#TERCERA OPCION PARA QUITAR UNA VENTANA EMERGENTE EN EDGE ANTES DE EXPLORAR LA PAGINA WEB
@pytest.mark.notrun
#paso 1 se entra en la url de la pagina web y quitamos la ventana emergente
def test_tres():
    driver = webdriver.Edge()
    driver.get("https://www.equifax.com.sv/efx-app-web-portal-sv/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.quit()
#





#CUARTA PRUEBA DE CROSS BROWSER TESTING EN UN SOLO SCRIPT
# La función selecciona el controlador adecuado según el navegador y ejecuta las acciones específicas para quitar la ventana emergente.
# Ademas, realiza la validación del título de la página y cierra el navegador al finalizar.
@pytest.mark.parametrize("browser", ["chrome", "firefox", "edge"])
def test_cross_browser(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.get("https://www.equifax.com.sv/efx-app-web-portal-sv/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Código para quitar la ventana emergente según el navegador
    if browser == "chrome":
        vemergente = driver.find_element(By.XPATH, "//span[contains(@aria-hidden,'true')]").click()
    elif browser == "firefox":
        vemergente2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[7]/div/div/div[1]/button/span"))
        )
        vemergente2.click()

    # Validación del título de la página
    try:
        assert "Equifax - Portal" == driver.title
        print(f"Prueba exitosa en {browser}: El título de la página es correcto")
    except AssertionError:
        print(f"Prueba fallida en {browser}: El título de la página no es correcto")

    driver.quit()