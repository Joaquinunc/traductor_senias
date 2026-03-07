import cv2
import mediapipe as mp
import pyautogui # lectura de GUI
from voicetry import text_voice, text_voice2

# captura de la camara
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2,    
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mpDraw = mp.solutions.drawing_utils
previous_gesture = ''
while True:
    ret, img = cap.read()
    if not ret:
        break
    
    #convertir imagen de BGR -> RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # deteccion de manos en base a la imagen capturada
    result = hands.process(imgRGB)

    mapHands = result.multi_hand_landmarks
    # si se reconoce el patron estandar de manos entramos
    if mapHands:
        
        for handlines in mapHands:
            # pintamos el patron en la imagen og NO en la deteccion
            mpDraw.draw_landmarks(img,handlines ,mp_hands.HAND_CONNECTIONS)
    
            #deteccion de posiciones de dedos especificas
            index_finger_y = handlines.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = handlines.landmark[mp_hands.HandLandmark.THUMB_TIP].y 
            
            if index_finger_y < thumb_y:
                hand_gesture = 'dedo indice apuntando hacia arriba'
                
            elif index_finger_y > thumb_y:
                hand_gesture = 'dedo indice apuntando hacia abajo'
               
            else:
                hand_gesture = ''
            
            #print(f"prev: {previous_gesture}. actual:{hand_gesture}")
            toggleact = previous_gesture != hand_gesture 
            #print(f"enter gestuer: {toggleact}")
            if toggleact:
                text_voice(hand_gesture)
                previous_gesture = hand_gesture
            

    #mostramos la imagen
    cv2.imshow('Image', img)
    # refrescamos constantemente
    cv2.waitKey(1)

