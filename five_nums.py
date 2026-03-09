import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

def gesture_classifier(handlines, mp_hands):
    # arreglo que tiene los vectores tridimensionales de las puntas de los dedos
    finger_tips = [
        mp_hands.HandLandmark.THUMB_TIP,
        mp_hands.HandLandmark.INDEX_FINGER_TIP,
        mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
        mp_hands.HandLandmark.RING_FINGER_TIP,
        mp_hands.HandLandmark.PINKY_TIP
    ]
    # eje y de la base de la falange del dedo medio
    mfinger_bot = handlines.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y

    # vector de 5 entradas, una para cada punta de un dedo
    vectorial_finger = [] 

    #recorremos el arreglo agregando 0s/1s segun la posicion sea abajo o arriba de mfinger_bot
    for tip in finger_tips:
        if handlines.landmark[tip].y < mfinger_bot:
            vectorial_finger.append(1)
        else:
            vectorial_finger.append(0)
   
    return vectorial_finger

def gesture_processor(handlines: landmark_pb2.NormalizedLandmarkList, mp_hands):
    #obtenemos el vector de posiciones para un gesto
    states = gesture_classifier(handlines, mp_hands)
    #print(f"states: {states}")
    # diccionario con tipos de gestos para cada posicion de manos
    gestos = {
        (0, 1, 0, 0, 0): "Uno",
        (0, 1, 1, 0, 0): "Dos",
        (0, 1, 1, 1, 0): "Tres",
        (0, 1, 1, 1, 1): "Cuatro",
        (1, 1, 1, 1, 1): "Cinco",
    }
    
    # obtenemos el valor en base al vector (en formato legible)
    hand_gesture = gestos.get(tuple(states), "")
    #print(f"hand_gesture: {hand_gesture}")
    return hand_gesture