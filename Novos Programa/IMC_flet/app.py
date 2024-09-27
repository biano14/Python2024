import flet as ft

def main(page: ft.Page):
    def acao(e):
        peso_val = peso.value.replace(',', '.')
        altura_val = altura.value.replace(',', '.')
        
        if peso_val.replace('.', '').isdigit() and altura_val.replace('.', '').isdigit():
            imc = float(peso_val) / (float(altura_val) ** 2)
            if imc < 17:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Muito abaixo do peso ideal'
            elif imc < 18.5:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Abaixo do peso ideal'
            elif imc < 24.9:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Peso ideal'
            elif imc < 29.9:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Acima do peso ideal'
            elif imc < 34.9:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Obesidade grau I'
            elif imc < 39.9:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Obesidade grau II'
            else:
                verificacao = f', seu IMC é {imc:.2f}, seu diagnóstico é: Obesidade grau III'
        else:
            verificacao = ", por favor, insira um peso e altura válidos."

        result.value = f'{nome.value} {verificacao}'
        nome.value = ''
        altura.value = ''
        peso.value = ''
        page.update()

    def ir_para_proximo_nome(e):
        peso.focus()
    
    def ir_para_proximo_altura(e):
        altura.focus()

    page.title = 'IMC'
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT

    nome = ft.TextField(label='Nome', on_submit=ir_para_proximo_nome)
    altura = ft.TextField(label='Altura', suffix_text='m', on_submit=acao)
    peso = ft.TextField(label='Peso', suffix_text='kg', on_submit=ir_para_proximo_altura)
    result = ft.Text(size=30)
    
    page.add(
        ft.Row(
            [ft.Text('IMC', size=40, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [peso],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [altura],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton('Calcular IMC', on_click=acao)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    page.update()

ft.app(main)
