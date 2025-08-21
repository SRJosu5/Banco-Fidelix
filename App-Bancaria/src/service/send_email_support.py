import smtplib

from email.mime.multipart import MIMEMultipart
from src.utils.error_handler import log_error
from email.mime.text import MIMEText

def send_email_support(client_name, client_case, description, client_email):
    try:

        sender = "labforprogra@gmail.com"
        addressee = "djcascante10@gmail.com"
        case = f"{client_name}, {client_case}"
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; text-align: center;">
            <h2 style="color: #007BFF;">Soporte Banco Fidelix</h2>
            <p>Correo del cliente: {client_email}</p>
            <p>Problema: {description}</p>
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