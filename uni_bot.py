from asyncio import exceptions
from logging import exception
import os
from time import sleep
from turtle import update
import requests


HTTP_API = os.environ['HTTP_API']

global empfangURL 
global sendURL 
global OFFSET
 




empfangURL = "http://api.telegram.org/bot" + HTTP_API + "/getUpdates"
sendUrl = "http://api.telegram.org/bot" + HTTP_API + "/sendMessage"
OFFSET = 0



sms = f"""\n\n
Hello , welcome to UNIVERSITYArea!
To get started, please reply with your registered User ID number.
You can find your ID in your backoffice on the dashboard.

Bonjour , bienvenue chez UNIVERSITYArea!
Pour commencer, veuillez répondre avec votre numéro d’utilisateur enregistré.
Vous pouvez trouver votre ID dans votre backoffice sur le tableau de bord.

Hola , bienvenido a UNIVERSITYArea!
Para comenzar, responda con su número de identificación de usuario registrado.
Puede encontrar su ID en su backoffice en el tablero de instrumentos.

مرحباً بك في "منطقة الجامعه"
للبدء ، يرجى الرد باستخدام اسم المستخدم المسجل لدينا
"يمكنك العثور على اسم المستخدم الخاص بك في المكتب الخلفي الخاص بك في القائمة الرئيسية.
"""
def willkomen(url):
    global OFFSET


    try:
        request_abfrage_system = requests.get(url + "?offset=" + str(OFFSET))
        abfrage = request_abfrage_system.json()
        data_laden = nachricht_extrahieren(abfrage)
        text = data_laden['message']['text']


        if text != False:
        

            OFFSET = data_laden['update_id'] + 1
            chat_id = data_laden['message']['chat']['id']
            nachricht_senden(chat_id, text)
            
    except requests.exceptions.ConnectionError:
        pass



def nachricht_extrahieren(dict):
    gesamt_array_abrufen = dict['result']
    message_array_abrufen = gesamt_array_abrufen[0]
    if gesamt_array_abrufen == []:
        return False
    else:
        message_array_abrufen = gesamt_array_abrufen[0]
        return message_array_abrufen


def nachricht_senden(chatId, message):
    requests.post(sendUrl + "?chat_id=" + str(chatId) + "&text="+ message) 





while True:
    willkomen(empfangURL)
    sleep(1)




