import flet as ft

def main(page: ft.Page):
    page.title = "Olá, mundo!"
    page.scroll = 'adaptive'
    
    # declarando as variaveis
    nome = ft.TextField(label='Nome')
    page.add(
        ft.Text('Olá, mundo!', size=30,color='#ffff00', weight='bold'),
        nome,
        ft.TextButton('Clique aqui')
    )
    page.update()
    
ft.app(main)