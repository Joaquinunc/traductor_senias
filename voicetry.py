import pyttsx3
"""
all_voices: muestra las voces disponibles para la libreria pyttsx3
"""
def all_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    separator = ' '
    f = open('voices.txt', 'w')
    for index, voice in enumerate(voices):
        f.write("Voice " + str(index) + ":\n")
        f.write(" - ID:" + voice.id + "\n")
        f.write(" - Name:" + voice.name + "\n")
        f.write(" - Languages:" +  
                separator.join(voice.languages) + "\n" )
        f.write(" - Gender:" + voice.gender + "\n")
        
"""
text_voice: traduce un input de texto a la salidad de voz
de audio. 
in: texto en formato escrito
out: audio del texto ingresado
"""
def text_voice(input:str):
    engine = pyttsx3.init()
    #modificamos a vos femenina es+f3, 
    engine.setProperty('voice', 'es+f3') 
    #disminuimos la velocidad
    engine.setProperty('rate',150)
    #engine.setProperty('pitch', 100)
    # decimos el texto input
    engine.say(input)
    engine.runAndWait()
    

def text_voice2(input:str):
    print(input)