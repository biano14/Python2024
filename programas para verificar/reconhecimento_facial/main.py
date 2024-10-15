import cv2
import numpy as np
import os

def captura(largura, altura):
    # classificadores
    classificador = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    classificador_olho = cv2.CascadeClassifier('haarcascade_eye.xml')
    
    # cria o diretório para armazenar as fotos, caso não exista
    if not os.path.exists('fotos'):
        os.makedirs('fotos')
    
    # câmera
    camera = cv2.VideoCapture(0)
    
    # amostras do usuário
    amostra = 1
    n_amostras = 25
    
    # recebe o ID do usuário
    id = input('Digite o ID do usuário: ')
    id = str(id)
    
    # mensagem indicando captura de imagens
    print('Capturando as imagens...')
    
    # loop de captura
    while True:
        conectado, imagem = camera.read()
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        faces_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(150, 150))
        
        # identifica a geometria das faces
        for (x, y, l, a) in faces_detectadas:
            cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
            regiao = imagem[y:y + a, x:x + l]
            regiao_cinza_olho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
            olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza_olho)
            
            # identificar a geometria dos olhos
            for (ox, oy, ol, oa) in olhos_detectados:
                cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)
                
                if np.average(imagem_cinza) > 110 and amostra <= n_amostras:
                    imagem_face = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
                    caminho = f'fotos/pessoa.{id}.{amostra}.jpg'
                    cv2.imwrite(caminho, imagem_face)
                    print(f'[foto] {amostra} de {id} capturada com sucesso em {caminho}.')
                    amostra += 1
        
        # Exibe a imagem com as faces detectadas
        cv2.imshow('Detectar faces', imagem)
        cv2.waitKey(1)
        
        if amostra > n_amostras:
            print("Faces capturadas com sucesso.")
            break
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print('Câmera encerrada.')
            break
    
    # encerra a captura
    camera.release()
    cv2.destroyAllWindows()

def get_imagem_com_id():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    faces = []
    ids = []
    
    for caminho_imagem in caminhos:
        imagem_face = cv2.cvtColor(cv2.imread(caminho_imagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminho_imagem)[-1].split('.')[1])
        ids.append(id)
        faces.append(imagem_face)
    
    return np.array(ids), faces

def treinamento():
    # cria os elementos de reconhecimento necessários
    eigenface = cv2.face.EigenFaceRecognizer_create()
    fisherface = cv2.face.FisherFaceRecognizer_create()
    lbph = cv2.face.LBPHFaceRecognizer_create()
    
    ids, faces = get_imagem_com_id()
    
    # treinando o algoritmo do programa
    print('Treinando...')
    eigenface.train(faces, ids)
    eigenface.write('classificadorEigen.yml')
    fisherface.train(faces, ids)
    fisherface.write('classificadorFisher.yml')
    lbph.train(faces, ids)
    lbph.write('classificadorLBPH.yml')
    
    # finaliza treinamento
    print('Treinamento finalizado com sucesso!')

# Programa principal
if __name__ == '__main__':
    # definir o tamanho da camera
    largura = 220
    altura = 220
    
    while True:
        # Menu
        print('0 - Sair do programa.')
        print('1 - Capturar imagem do usuário.')
        print('2 - Treinar sistema.')
        
        opcao = input('Opção desejada: ')
        
        match opcao:
            case '0':
                print('Programa encerrado')
                break
            case '1':
                captura(largura, altura)
                continue
            case '2':
                treinamento()
                continue
            case _:
                print('Opção inválida.')