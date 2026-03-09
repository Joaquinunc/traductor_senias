import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

def gesture_classifier(handlines, mp_hands):
    ifinger_top = handlines.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    thumb_y = handlines.landmark[mp_hands.HandLandmark.THUMB_TIP].y 
    thumb_ip_y = handlines.landmark[mp_hands.HandLandmark.THUMB_IP].y
    mfinger_top = handlines.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    rfinger_top = handlines.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pfinger_top = handlines.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    mfinger_bot = handlines.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
    thumb_x = handlines.landmark[mp_hands.HandLandmark.THUMB_TIP].x
    ifinger_x = handlines.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x 
    return ifinger_top, thumb_y, mfinger_top, rfinger_top, pfinger_top, thumb_x, ifinger_x, mfinger_bot, thumb_ip_y 

def gesture_processor(handlines: landmark_pb2.NormalizedLandmarkList, mp_hands):

     #deteccion de posiciones de dedos especificas
    ifinger_top,thumb_y, mfinger_top, rfinger_top, pfinger_top, thumb_x, ifinger_x, mfinger_bot, thumb_ip_y = gesture_classifier(handlines, mp_hands)
    # matcheo de patrones
    # caso 1: ☝️
    isOne = ((ifinger_top < mfinger_bot)
             and (mfinger_top > mfinger_bot) and(rfinger_top > mfinger_bot) and (pfinger_top> mfinger_bot)
             and (thumb_y < mfinger_top) and (thumb_y < pfinger_top) and (thumb_y < rfinger_top))
    #✌️
    isTwo = ((ifinger_top < mfinger_bot)
             and (mfinger_top < mfinger_bot) and(rfinger_top > mfinger_bot) and (pfinger_top> mfinger_bot)
             and (thumb_y < pfinger_top) and (thumb_y < rfinger_top))
    #tres dedos hacia arriba
    isThree = ((ifinger_top < mfinger_bot)
             and (mfinger_top < mfinger_bot) and(rfinger_top < mfinger_bot) and (pfinger_top> mfinger_bot)
             and (thumb_y < pfinger_top))
    #cuatro dedos hacia arriba
    isFour = ((ifinger_top < mfinger_bot)
             and (mfinger_top < mfinger_bot) and(rfinger_top < mfinger_bot) and (pfinger_top< mfinger_bot)
             and (thumb_y > mfinger_bot))
    #✋
    isFive = ((ifinger_top < mfinger_bot)
             and (mfinger_top < mfinger_bot) and(rfinger_top < mfinger_bot) and (pfinger_top< mfinger_bot)
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
