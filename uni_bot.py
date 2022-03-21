from telegram.ext import *
import os


HTTP_API = os.environ['HTTP_API']









def sende_wenn_nachricht_angekommen(update, context):


    text = update.message.text
    antworten_darauf = nachricht_erstellen(text)
   
    update.message.reply_text(antworten_darauf)



def nachricht_erstellen(input_text, input_id):
    if input_text == "/start":
        return f"""\n\n
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
  







    if input_id == "/system":
        return f"""\n\n
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
  




def comunication_with_telegram_api():
    updater = Updater(HTTP_API)
    controll_sms = updater.dispatcher
    controll_sms.add_handler(MessageHandler(Filters.text, sende_wenn_nachricht_angekommen))
    updater.start_polling(0)


















        



    
if __name__=="__main__":
    comunication_with_telegram_api()


