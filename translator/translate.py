from googletrans import Translator

def translate(text):
    translator = Translator()
    tranlation = translator.translate(text = text, dest= 'de')
    return tranlation.text