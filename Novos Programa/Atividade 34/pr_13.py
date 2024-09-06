# escolher diretorio comando: cxfreeze app.py --target-dir autoteste
import pyautogui as auto
import time

auto.PAUSE = 0.5

# Abre o navegador e acessa o GitHub
auto.press('win')
auto.write('chrome')
auto.press('enter')
auto.hotkey('alt','space')
auto.press('x')
time.sleep(2)  # Espera o navegador abrir
auto.write('youtube.com')
auto.press('enter')
time.sleep(5)  # Espera a página carregar
for i in range(4):
    auto.press('tab')
time.sleep(2)  # Espera o navegador abrir
auto.write('videoaulas sobre Python')
auto.press('enter')