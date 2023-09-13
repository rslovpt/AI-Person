from scripts.main_network import network
from scripts.json import json_ex as js
from scripts.speech_rec import speech_rec as sr
from scripts.tts import text_to_speech as tts

system_booted = False

modules = {}

settings = {
    'speaking_enabled':False,
    'speech_rec_enabled':False,
}

class Boot:
    
    def __init__(self):
        modules['network'] = network()
        if settings['speaking_enabled']:
            modules['tts'] = tts(js("VOICE").load_var())
            modules['tts'].load_module()
        if settings['speech_rec_enabled']:
            modules['sr'] = sr().load_module()
            modules['sr'].load_module()
            
        global system_booted
        system_booted = True
        print("Modules Loaded: " + str(len(modules)))

        return

Boot()

while (1):
    if system_booted:
        inputed = None
        response = None
        if settings['speech_rec_enabled']:
            pass
        else:
            inputed = input("Talk >> ")

        response = modules['network'].input_recieved(inputed)

        if settings['speaking_enabled']:
            pass