import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

def gesture_classifier(handlines, mp_hands):
    ifinger_top = handlines.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    thumb_y = handlines.landmark[mp_hands.HandLandmark.THUMB_TIP].y 
    mfinger_top = handlines.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    rfinger_top = handlines.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pfinger_top = handlines.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_x = handlines.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    ifinger_x = handlines.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x 
    return ifinger_top, thumb_y, mfinger_top, rfinger_top, pfinger_top, thumb_x, ifinger_x 

def gesture_processor(handlines: landmark_pb2.NormalizedLandmarkList, mp_hands):

     #deteccion de posiciones de dedos especificas
    ifinger_top,thumb_y, mfinger_top, rfinger_top, pfinger_top, thumb_x, ifinger_x = gesture_classifier(handlines, mp_hands)
    # matcheo de patrones
    # caso 1: ☝️
    isOne = ((ifinger_top < thumb_y)
             and (mfinger_top > thumb_y) and(rfinger_top > thumb_y) and (pfinger_top> thumb_y)
             and (thumb_x < ifinger_x))
    #✌️
    isTwo = ((ifinger_top < thumb_y)
             and (mfinger_top < thumb_y) and(rfinger_top > thumb_y) and (pfinger_top> thumb_y)
             and (thumb_x < ifinger_x))
    #tres dedos hacia arriba
    isThree = ((ifinger_top < thumb_y)
             and (mfinger_top < thumb_y) and(rfinger_top < thumb_y) and (pfinger_top> thumb_y)
             and (thumb_x < ifinger_x))
    #cuatro dedos hacia arriba
    isFour = ((ifinger_top < thumb_y)
             and (mfinger_top < thumb_y) and(rfinger_top < thumb_y) and (pfinger_top< thumb_y)
             and (thumb_x < ifinger_x))
    #✋
    isFive = ((ifinger_top < thumb_y)
             and (mfinger_top < thumb_y) and(rfinger_top < thumb_y) and (pfinger_top< thumb_y)
    )

    if isOne:
        hand_gesture = 'Uno'
    elif isTwo:
        hand_gesture = 'Dos' 
    elif isThree:
        hand_gesture = 'Tres'
    elif isFour:
        hand_gesture = 'Cuatro'
    elif isFive:
        hand_gesture = 'Cinco'
    else:
        hand_gesture = ''

    return hand_gesture 
