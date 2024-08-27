# importa a biblioteca de automação
# NOTE: instale a biblioteca: pip install pyautogui
import pyautogui as auto
auto.PAUSE = 0.3                                  


auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita a palavra "chrome"
auto.press('enter') # aperta "Enter"
auto.hotkey('alt','space')
auto.press('x')
auto.write('github.com')
auto.press('enter')
# entrar na página de login do github
for i in range(12):
    auto.press('tab')
auto.press('enter')