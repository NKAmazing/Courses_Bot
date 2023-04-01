import discord
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializar objeto de cliente de Discord
intents = discord.Intents.default()
intents.members = True  # habilita la búsqueda de miembros del servidor

client = discord.Client(intents=intents)

# Inicializar objeto webdriver de Firefox
driver = webdriver.Firefox()

# Definir función para procesar mensajes entrantes
@client.event
async def on_message(message):
    # Ignorar mensajes del bot
    if message.author == client.user:
        return

    # Procesar mensaje entrante
    if message.content.startswith('-buscar'):
        print(f"Comando '!buscar' detectado en el mensaje: {message.content}")
        term = message.content.split('-buscar ', 1)[1]
        print(f"Término de búsqueda extraído: {term}")
        results = search(term)
        response = '\n'.join([f"{result['title']}: {result['url']}" for result in results])

        # Responder al mensaje
        print(f"Enviando respuesta: {response}")
        await message.channel.send(response)

    if message.content.startswith('-hola'):
        print(f"Comando '-hola' detectado en el mensaje: {message.content}")
        await message.channel.send('Hola Nico!')



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

if __name__ == '__main__':
    # Cargar variables de entorno
    load_dotenv()

    # Iniciar cliente de Discord
    client.run(os.getenv('DISCORD_TOKEN'))



