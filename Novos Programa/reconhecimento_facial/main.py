# importa as bibliotecas
import cv2
import numpy as np
import os

def captura(largura, altura):
    # classificadores
    classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classificador_olho = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    # camera
    camera = cv2.VideoCapture(0)
    
    
    #amostras do usuario
    amostra = 1
    n_amostras = 25
    
    # recebe o id do usuário
    id = input('Digite o ID do usuário: ')
    
    # mensagem indicando captura de imagens
    print('Capturando as imagens...')
    
    # loop
    while True:
        conectado, imagem = camera.read()
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        print(np.average(imagem_cinza))
        faces_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.5,minSize=(150, 150))
        
        # identifica a geometria das faces
        for(x, y, l, a) in faces_detectadas:
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,0,255), 2)
            regiao = imagem[y:y + a, y:y + l]
            regiao_cinza_olho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
            olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza_olho)
            #identificar a geometria dos olhos
            for (ox, oy, ol, oa) in olhos_detectados:
                cv2.rectangle(regiao, (ox, oy), (ox+ ol , oy+ oa), (0,255,0), 2)
                
                if np.average(imagem_cinza) > 110 and amostra <= n_amostras:
                    imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
                    caminho = f'fotos/pessoa.{id}.{amostra}.jpg', imagem_face
                    cv2.imwrite(caminho, imagem)
                    print(f'[foto] {amostra} de {id} capturada com sucesso em {caminho}.')
                    amostra += 1
        cv2.imshow('Detectar faces', imagem)
        cv2.waitKey(1)
        
        if (amostra >= n_amostras + 1):
            print("Faces capturadas com sucesso.")
            break
        elif cv2.waitKey(1) == ord('q'):
            print('Câmera encerrada.')
            break
    # encerra a captura
    camera.release()
    cv2.destroyAllWindows()
    # fim de função
# Programa principal
if __name__ == '__main__':
    #definir o tamanho da camera
    largura = 220
    altura = 220
    
    while True:
        # Menu
        print('0 - Sair do programa.')
        print('1 - Capturar imagem do usuario.')
        
        opcao = input('Opção desejada:')
        
        match opcao:
            case '0':
                print('Programa encerrado')
                break
            case '1':
                captura(largura, altura)
                continue