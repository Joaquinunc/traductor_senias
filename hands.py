import mediapipe as mp
import cv2
import time
import math

#utlizaremos una clase "MANOS"
class handDetect():
    

    # inicializacion de parametros de deteccion
    def __init__(self, mode=False, maxManos=2, Confdeteccion=0.5, Confsegui=0.5):
        self.mode = mode
        self.maxManos = maxManos
        self.Confdeteccion = Confdeteccion
        self.Confsegui = Confsegui

        # obj que detectan/dibujan manos
        self.mpHands = mp.solutions.hands
        self.manos = self.mpmanos.Hands(self.mode, self.maxManos, self.Confdeteccion, self.Confsegui)
        self.mpDraw = mp.solutions.drawing_utils
        self.tip = [4,8,12,16,20]
    
    # metodo para encontrar las manos
    def handsFinder(self, img, draw = True):
        
         #convertir imagen de BGR -> RGB
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # deteccion de manos en base a la imagen capturada
        self.result = self.manos.process(imgRGB)
        
        mapHands = self.result.multi_hand_landmarks
        # si se reconoce el patron estandar de manos entramos
        if mapHands:
            
            for handlines in mapHands:
                # pintamos el patron en la imagen og NO en la deteccion
                self.mpDraw.draw_landmarks(img,handlines ,self.mpHands.HAND_CONNECTIONS)
        return img
    
    #metodo para encontrar la posicion
    def posFinder(self, img, Manonum = 0, draw=True):
        xlist = []
        ylist = []
        bbox = []
        self.lista = []

        if self.resultados.multi_hand_landmarks:
            miMano = self.resultados.multi_hand_landmarks[Manonum]
            
            for id, lm in enumerate(miMano.landmark):
                alto, ancho, c = img.shape # dimensiones de los fps
                cx,cy = int(lm.x * ancho), int(lm.y * alto) # convertir a pixeles
                xlist.append(cx)
                ylist.append(cy)
                self.lista.append([id, cx,cy])

                if draw:
                    cv2.circle(img, (cx,cy), 5, (0,0,0), cv2.FILLED)
            

            xmin, xmax = min(xlist), max(xlist)
            ymin, ymax = min(ylist), max(ylist)
            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin-20, ymin -20), (xmax+20, ymax +20), (0,255,0), 2)
        
        return self.lista, bbox
    

    #