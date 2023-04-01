import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
import os

# Inicializar objeto webdriver de Firefox
driver = WebDriver()

# Inicializar objeto webdriver de Chrome
# driver = webdriver.Chrome()

# Definir función de búsqueda
def search(term):
    # Acceder a la página de Código Facilito
    driver.get('https://www.codigofacilito.com/')

    # Encontrar el campo de búsqueda y escribir el término a buscar
    search_field = driver.find_element_by_name('search')
    search_field.send_keys(term)
    search_field.send_keys(Keys.RETURN)

    # Encontrar los resultados y retornarlos
    results = driver.find_elements_by_css_selector('.course__title')
    return [{'title': result.text, 'url': result.get_attribute('href')} for result in results]

