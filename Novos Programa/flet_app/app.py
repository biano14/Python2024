# Importando biblioteca gráfica
import flet as ft 


def main(page: ft.Page):
    def acao(e):
        result.value = texto.value
        page.update()
    # Configuração de janela
    page.title = "Meu Flet App"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT

    # Declaração de variaveis
    texto = ft.TextField(label="Digite aqui seu texto", on_change=acao)
    result = ft.Text(size=30)

    # Conteudo das janelas
    page.add(
        texto,
        result
    )

    # Atualização do app
    page.update()

# Execução da aplicação
ft.app(main)