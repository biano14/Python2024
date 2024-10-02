# import flet as ft
# from pessoa import *
# from manipulador import *

# def main(page: ft.Page):
#     p = Pessoa(0, '', '', '', '')
#     m = Manipulador()
#     usuarios = []

#     def criar_arquivo(e):
#         novo_arquivo = nome_arquivo.value
#         if novo_arquivo:
#             mensagem.value = m.criar_arquivo(novo_arquivo)
#             nome_arquivo.value = ''
#             page.update()

#     def abrir_arquivo(e):
#         abrir_arquivo_nome = nome_arquivo.value
#         try:
#             usuarios.clear()
#             usuarios.extend(m.abrir_arquivo(abrir_arquivo_nome))
#             mensagem.value = f'Arquivo aberto: {abrir_arquivo_nome}.json.'
#             exibir_usuarios()
#         except Exception as e:
#             mensagem.value = f'Não foi possível abrir o arquivo. {e}.'
#         page.update()

#     def exibir_usuarios():
#         lista_usuarios.value = ''
#         for i, usuario in enumerate(usuarios):
#             detalhes = ', '.join([f"{campo.capitalize()}: {usuario[campo]}" for campo in usuario])
#             lista_usuarios.value += f'Usuário {i}: {detalhes}\n{"-"*30}\n'
#         page.update()

#     def salvar_usuario(e):
#         try:
#             p.codigo = len(usuarios)
#             p.nome = nome.value
#             p.cpf = cpf.value
#             p.email = email.value
#             p.profissao = profissao.value
            
#             usuario = {
#                 'codigo': p.codigo,
#                 'nome': p.nome,
#                 'cpf': p.cpf,
#                 'email': p.email,
#                 'profissao': p.profissao
#             }
#             usuarios.append(usuario)
#             m.salvar_dados(usuarios, nome_arquivo.value)
#             mensagem.value = 'Usuário salvo com sucesso!'
#             exibir_usuarios()
#             limpar_campos()
#         except Exception as e:
#             mensagem.value = f'Não foi possível salvar o usuário. {e}.'
#         page.update()

#     def limpar_campos():
#         nome.value = ''
#         cpf.value = ''
#         email.value = ''
#         profissao.value = ''
#         codigo_usuario.value = ''
#         page.update()

#     def alterar_usuario(e):
#         try:
#             codigo = int(codigo_usuario.value) 
#             if 0 <= codigo < len(usuarios):
#                 usuario = usuarios[codigo]
#                 nome.value = usuario['nome']
#                 cpf.value = usuario['cpf']
#                 email.value = usuario['email']
#                 profissao.value = usuario['profissao']
#             else:
#                 mensagem.value = 'Código de usuário inválido.'
#         except ValueError:
#             mensagem.value = 'Por favor, insira um código válido.'
#         page.update()

#     def confirmar_alterar(e):
#         try:
#             codigo = int(codigo_usuario.value) 
#             if 0 <= codigo < len(usuarios):
#                 usuarios[codigo]['nome'] = nome.value
#                 usuarios[codigo]['cpf'] = cpf.value
#                 usuarios[codigo]['email'] = email.value
#                 usuarios[codigo]['profissao'] = profissao.value
#                 m.salvar_dados(usuarios, nome_arquivo.value)
#                 mensagem.value = 'Usuário atualizado com sucesso!'
#                 exibir_usuarios()
#                 limpar_campos()
#             else:
#                 mensagem.value = 'Código de usuário inválido.'
#         except Exception as e:
#             mensagem.value = f'Não foi possível atualizar o usuário. {e}.'
#         page.update()

#     def deletar_usuario(e):
#         try:
#             codigo = int(codigo_usuario.value) 
#             if 0 <= codigo < len(usuarios):
#                 confirmacao_dialog = ft.AlertDialog(
#                     title=ft.Text("Confirmação de Deleção"),
#                     content=ft.Text(f"Deseja realmente deletar o usuário {usuarios[codigo]['nome']}?"),
#                     actions=[
#                         ft.TextButton("Sim", on_click=lambda e: confirmar_deletar(codigo)),
#                         ft.TextButton("Não", on_click=lambda e: page.close(confirmacao_dialog))
#                     ],
#                     on_dismiss=handle_dismiss
#                 )
#                 page.open(confirmacao_dialog)
#             else:
#                 mensagem.value = 'Código de usuário inválido.'
#         except ValueError:
#             mensagem.value = 'Por favor, insira um código válido.'
#         page.update()

#     def handle_dismiss(e):
#         mensagem.value = "Ação de deleção cancelada."

#     def confirmar_deletar(codigo):
#         try:
#             nome_deletado = usuarios[codigo]['nome']
#             del usuarios[codigo]
#             m.salvar_dados(usuarios, nome_arquivo.value)
#             mensagem.value = f'Usuário {nome_deletado} deletado com sucesso.'
#             exibir_usuarios()
#             limpar_campos()
#         except Exception as e:
#             mensagem.value = f'Não foi possível deletar o usuário. {e}.'
#         page.update()

#     page.title = "Gerenciador de Usuários"
#     page.vertical_alignment = ft.MainAxisAlignment.START

#     nome_arquivo = ft.TextField(label='Nome do Arquivo', on_submit=abrir_arquivo)
#     nome = ft.TextField(label='Nome')
#     cpf = ft.TextField(label='CPF')
#     email = ft.TextField(label='Email')
#     profissao = ft.TextField(label='Profissão')
#     codigo_usuario = ft.TextField(label='Código do Usuário')

#     mensagem = ft.Text("")
#     lista_usuarios = ft.TextField(label='Usuários', multiline=True, width=400, height=400, read_only=True)

#     usuarios_container = ft.Container(
#         content=lista_usuarios,
#         width=400,
#         height=400,
#         alignment=ft.alignment.center
#     )

#     page.add(
#         nome_arquivo,
#         ft.Row([ft.ElevatedButton('Criar Arquivo', on_click=criar_arquivo),
#                  ft.ElevatedButton('Abrir Arquivo', on_click=abrir_arquivo)]),
#         nome,
#         cpf,
#         email,
#         profissao,
#         ft.ElevatedButton('Salvar Usuário', on_click=salvar_usuario),
#         codigo_usuario,
#         ft.Row([ft.ElevatedButton('Alterar Usuário', on_click=alterar_usuario),
#                  ft.ElevatedButton('Confirmar Alteração', on_click=confirmar_alterar),
#                  ft.ElevatedButton('Deletar Usuário', on_click=deletar_usuario)]),
#         mensagem,
#         ft.Container(content=usuarios_container, alignment=ft.alignment.center)
#     )

#     page.update()

# ft.app(main)
import flet as ft
from pessoa import *
from manipulador import *

def main(page: ft.Page):
    p = Pessoa(0, '', '', '', '')
    m = Manipulador()
    page.window.maximized = True
    usuarios = []

    def criar_arquivo(e):
        novo_arquivo = nome_arquivo.value
        if novo_arquivo:
            mensagem.value = m.criar_arquivo(novo_arquivo)
            nome_arquivo.value = ''
            page.update()

    def abrir_arquivo(e):
        abrir_arquivo_nome = nome_arquivo.value
        try:
            usuarios.clear()
            usuarios.extend(m.abrir_arquivo(abrir_arquivo_nome))
            mensagem.value = f'Arquivo aberto: {abrir_arquivo_nome}.json.'
            exibir_usuarios()
        except Exception as e:
            mensagem.value = f'Não foi possível abrir o arquivo. {e}.'
        page.update()

    def exibir_usuarios():
        lista_usuarios.value = ''
        for i, usuario in enumerate(usuarios):
            detalhes = '\n'.join([f"{campo.capitalize()}: {usuario[campo]}" for campo in usuario])
            lista_usuarios.value += f'Usuário {i}:\n{detalhes}\n{"-"*30}\n'
        page.update()

    def salvar_usuario(e):
        try:
            p.codigo = len(usuarios)
            p.nome = nome.value
            p.cpf = cpf.value
            p.email = email.value
            p.profissao = profissao.value
            
            usuario = {
                'codigo': p.codigo,
                'nome': p.nome,
                'cpf': p.cpf,
                'email': p.email,
                'profissao': p.profissao
            }
            usuarios.append(usuario)
            m.salvar_dados(usuarios, nome_arquivo.value)
            mensagem.value = 'Usuário salvo com sucesso!'
            exibir_usuarios()
            limpar_campos()
        except Exception as e:
            mensagem.value = f'Não foi possível salvar o usuário. {e}.'
        page.update()

    def limpar_campos():
        nome.value = ''
        cpf.value = ''
        email.value = ''
        profissao.value = ''
        codigo_usuario.value = ''
        page.update()

    def alterar_usuario(e):
        try:
            codigo = int(codigo_usuario.value) 
            if 0 <= codigo < len(usuarios):
                usuario = usuarios[codigo]
                nome.value = usuario['nome']
                cpf.value = usuario['cpf']
                email.value = usuario['email']
                profissao.value = usuario['profissao']
            else:
                mensagem.value = 'Código de usuário inválido.'
        except ValueError:
            mensagem.value = 'Por favor, insira um código válido.'
        page.update()

    def confirmar_alterar(e):
        try:
            codigo = int(codigo_usuario.value) 
            if 0 <= codigo < len(usuarios):
                usuarios[codigo]['nome'] = nome.value
                usuarios[codigo]['cpf'] = cpf.value
                usuarios[codigo]['email'] = email.value
                usuarios[codigo]['profissao'] = profissao.value
                m.salvar_dados(usuarios, nome_arquivo.value)
                mensagem.value = 'Usuário atualizado com sucesso!'
                exibir_usuarios()
                limpar_campos()
            else:
                mensagem.value = 'Código de usuário inválido.'
        except Exception as e:
            mensagem.value = f'Não foi possível atualizar o usuário. {e}.'
        page.update()
    def deletar_usuario(e):
        try:
            codigo = int(codigo_usuario.value)
            if 0 <= codigo < len(usuarios):
                confirmacao_dialog = ft.AlertDialog(
                    title=ft.Text("Confirmação de Deleção"),
                    content=ft.Text(f"Deseja realmente deletar o usuário {usuarios[codigo]['nome']}?"),
                    actions=[
                        ft.TextButton("Sim", on_click=(lambda e: (confirmar_deletar(codigo), page.close(confirmacao_dialog)))),
                        ft.TextButton("Não", on_click=lambda e: page.close(confirmacao_dialog))
                    ]
                )
                page.open(confirmacao_dialog)
            else:
                mensagem.value = 'Código de usuário inválido.'
        except ValueError:
            mensagem.value = 'Por favor, insira um código válido.'
        page.update()


    def confirmar_deletar(codigo):
        try:
            nome_deletado = usuarios[codigo]['nome']
            del usuarios[codigo]
            m.salvar_dados(usuarios, nome_arquivo.value)
            mensagem.value = f'Usuário {nome_deletado} deletado com sucesso.'
            exibir_usuarios()
            limpar_campos()
        except Exception as e:
            mensagem.value = f'Não foi possível deletar o usuário. {e}.'
        page.update()

    page.title = "Gerenciador de Usuários"
    page.vertical_alignment = ft.MainAxisAlignment.START

    nome_arquivo = ft.TextField(label='Nome do Arquivo', on_submit=abrir_arquivo)
    nome = ft.TextField(label='Nome')
    cpf = ft.TextField(label='CPF')
    email = ft.TextField(label='Email')
    profissao = ft.TextField(label='Profissão')
    codigo_usuario = ft.TextField(label='Código do Usuário')

    mensagem = ft.Text("")
    lista_usuarios = ft.TextField(label='Usuários', multiline=True, width=400, height=400, read_only=True)

    usuarios_container = ft.Container(
        content=lista_usuarios,
        width=400,
        height=400,
        alignment=ft.alignment.center
    )

    page.add(
        nome_arquivo,
        ft.Row([ft.ElevatedButton('Criar Arquivo', on_click=criar_arquivo),
                 ft.ElevatedButton('Abrir Arquivo', on_click=abrir_arquivo)]),
        nome,
        cpf,
        email,
        profissao,
        ft.ElevatedButton('Salvar Usuário', on_click=salvar_usuario),
        codigo_usuario,
        ft.Row([ft.ElevatedButton('Alterar Usuário', on_click=alterar_usuario),
                 ft.ElevatedButton('Confirmar Alteração', on_click=confirmar_alterar),
                 ft.ElevatedButton('Deletar Usuário', on_click=deletar_usuario)]),
        mensagem,
        ft.Container(content=usuarios_container, alignment=ft.alignment.center)
    )

    page.update()

ft.app(main)
