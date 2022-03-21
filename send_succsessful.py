import smtplib 
from email.message import EmailMessage
import os
user_mail = os.environ['EMAIL_ADDRESS']
user_password = os.environ['EMAIL_USER_PASSWORD']
def main(empfängernachname):
    sub = "Successful Registration"
    SMS = f"""\n\n
    <h1 style="color:red"> Ari System GmbH welcomes you {empfängernachname} </h1>
    """
    msg = EmailMessage()
    msg['Subject'] = sub
    msg['From'] = "Ari System<support@goquanto.de>"
    msg['To'] = "ari.bermeki@icloud.com"
    msg.set_content(SMS, subtype="html")
    with smtplib.SMTP('smtp.ionos.de', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(user_mail, user_password)
        smtp.send_message(msg)


if __name__ == "__main__":
    main() 
