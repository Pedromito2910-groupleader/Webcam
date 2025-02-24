'''
   Progamador....: (C) 2025 Pedro Sousa
   Data..........: 05/02/2025
   Observações...: Exemplo prático de utilização do OpenCV
'''

import cv2 as cv

webcam = cv.VideoCapture(0)

if not webcam.isOpened:
    print("Não foi possível abrir à webcam!")
    exit()
   
while True:
    retorno, frame = webcam.read()

    if not retorno:
        print("Erro na captura da webcam")
        break
    
    frameTonsCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #frameCanny = cv.Canny(frame, 100, 200)
    #frameBlur = cv.blur(frame, (15, 15))
    (status, framePB) = cv.threshold(frameTonsCinza, 127, 255, cv.THRESH_BINARY)

    cv.imshow('Imagem Capturada pela webcam', frame )
    #cv.imshow('Imagem Tons de Cinza', frameTonsCinza)
    #cv.imshow('Imagem Canny', frameCanny)
    #cv.imshow('Imagem Blur', frameBlur)
    cv.imshow('Imagem Preto e Branco', framePB)
    
      
    if cv.waitKey (1) == ord('q'):
      break
    
   
webcam.release() 
cv.destroyAllWindows() 