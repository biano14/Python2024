# escolher diretorio comando: cxfreeze app.py --target-dir autoteste
import pyautogui as auto
import time
import os

auto.PAUSE = 0.5

# Abre o navegador e acessa o GitHub
auto.press('win')
auto.write('chrome')
auto.press('enter')
time.sleep(2)  # Espera o navegador abrir
auto.write('youtube.com')
auto.press('enter')
time.sleep(5)  # Espera a página carregar

# Navega para criar um novo repositório
# Certifique-se de que as coordenadas estejam corretas para o botão de "+" ou "Novo repositório"
for i in range(5):
    auto.press('tab')
time.sleep(2)  # Espera o navegador abrir
auto.write('Python')
auto.press('enter')