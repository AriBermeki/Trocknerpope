import smtplib 
from email.message import EmailMessage
import os


user_mail = os.environ['EMAIL_ADDRESS']
user_password = os.environ['EMAIL_USER_PASSWORD']
def send_sys(empfänger_vorname, empfänger_email):
    sub = "Successful Registration"
    SMS = f"""\n\n
    <h1 style="color:red"> Ari System GmbH welcomes you {empfänger_vorname} </h1>
    """
    msg = EmailMessage()
    msg['Subject'] = sub
    msg['From'] = "Ari System<support@goquanto.de>"
    msg['To'] = f"{empfänger_email}"
    msg.set_content(SMS, subtype="html")
    with smtplib.SMTP('smtp.ionos.de', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user_mail, user_password)
        smtp.send_message(msg)





