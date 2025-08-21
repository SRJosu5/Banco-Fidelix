import smtplib, random

from email.mime.multipart import MIMEMultipart
from src.utils.error_handler import log_error
from email.mime.text import MIMEText

def send_email(email):
    try:
        global token

        token = random.randint(100000,999999)

        sender = "labforprogra@gmail.com"
        addressee = email
        case = "Banco Fidelex"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; text-align: center;">
            <h2 style="color: #007BFF;">Codigo de verifcacion</h2>
            <p>Codigo de verificacion para cambiar contraseña: <span style="color: #28A745;">{token}</span></p>
        </body>
        </html>
        """

        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = addressee
        message['Subject'] = case

        message.attach(MIMEText(body, 'html'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls() 
            server.login(sender, "pogd zrjg sohp xqyh")
            text = message.as_string()
            server.sendmail(sender, addressee, text)
            server.quit()
            
            return True
        except Exception as e:
            print(f"Hubo un error: {e}")
            return False
        
    except Exception as error:
        log_error(error)