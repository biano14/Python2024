import winapps

for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data de instalação: {item.version}.')
    print(f'Data de publicação: {item.publisher}.')
    print(f'Local de Desinstalação: {item.uninstall_string}.')
    print('-'*50)
    