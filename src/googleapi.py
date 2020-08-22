#-*- coding: utf-8 -*-
from googletrans import Translator
translator = Translator()

 
result = translator.translate('elma', src='tr', dest='en')
    
print(result.text) 


