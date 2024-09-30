import flet as ft

def main(page: ft.Page):
    #testando o shape_selector
    def calcular_area(e):
        shape = shape_selector.value
        b = base.value.replace(',', '.')
        h = altura.value.replace(',', '.')
        r = raio.value.replace(',', '.')

        if shape == 'Quadrilátero':
            if b.replace('.', '').isdigit() and h.replace('.', '').isdigit():
                area = calcular_quadrilatero(float(b), float(h))
                result.value = f'Área do quadrilátero: {area:.2f}'
            else:
                result.value = 'Por favor, insira base e altura válidas.'
        
        elif shape == 'Triângulo':
            if b.replace('.', '').isdigit() and h.replace('.', '').isdigit():
                area = calcular_triangulo(float(b), float(h))
                result.value = f'Área do triângulo: {area:.2f}'
            else:
                result.value = 'Por favor, insira base e altura válidas.'
        
        elif shape == 'Círculo':
            if r.replace('.', '').isdigit():
                area = calcular_circulo(float(r))
                result.value = f'Área do círculo: {area:.2f}'
            else:
                result.value = 'Por favor, insira um raio válido.'

        page.update()

    def calcular_quadrilatero(b, h):
        return b * h

    def calcular_triangulo(b, h):
        return (b * h) / 2

    def calcular_circulo(r):
        return 3.14 * r ** 2

    page.title = 'Calculadora de Áreas'
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT

    # Opções que aparecem no seletor (ft.dropdown.option)
    shape_selector = ft.Dropdown(
        label='Selecione a figura:',
        options=[
            ft.dropdown.Option('Quadrilátero'),
            ft.dropdown.Option('Triângulo'),
            ft.dropdown.Option('Círculo'),
        ],
        on_change=lambda e: mudar_inputs()
    )
    
    base = ft.TextField(label='Base', suffix_text='m', on_submit=calcular_area)
    altura = ft.TextField(label='Altura', suffix_text='m', on_submit=calcular_area)
    raio = ft.TextField(label='Raio', suffix_text='m', on_submit=calcular_area)
    
    result = ft.Text(size=20)
    
    # teste para ocultar campos que não estão em uso
    altura.visible = False
    base.visible = False
    raio.visible = False

    def mudar_inputs():
        if shape_selector.value == 'Quadrilátero' or shape_selector.value == 'Triângulo':
            base.visible = True
            altura.visible = True
            raio.visible = False
        elif shape_selector.value == 'Círculo':
            base.visible = False
            altura.visible = False
            raio.visible = True
        page.update()

    page.add(
        shape_selector,
        base,
        altura,
        raio,
        ft.ElevatedButton('Calcular Área', on_click=calcular_area),
        result
    )

ft.app(main)
