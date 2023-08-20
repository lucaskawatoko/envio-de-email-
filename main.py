import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from segredos.segredos import *

def enviar_email(destinatarios, assunto, corpo, anexos=[]):
    fromaddr = e__mail

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, senhas)

    for toaddr in destinatarios:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = assunto

        # Corpo do e-mail em HTML
        html_corpo = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }}
                .container {{
                    background-color: #00000f;
                    color: #ffffff;
                    border-radius: 10px;
                    padding: 20px;
                    margin: 20px auto;
                    width: 80%;
                }}
                .header {{
                    background-color: #007bff;
                    color: #ffffff;
                    padding: 10px;
                    border-radius: 10px 10px 0 0;
                    text-align: center;
                }}
                .content {{
                    padding: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>{assunto}</h1>
                </div>
                <div class="content">
                    <p>{corpo}</p>
                </div>
            </div>
        </body>
        </html>
        """

        msg.attach(MIMEText(html_corpo, 'html'))

        for anexo in anexos:
            filename = os.path.basename(anexo)
            attachment = open(anexo, 'rb')

            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {filename}")
            msg.attach(part)

            attachment.close()

        server.sendmail(fromaddr, toaddr, msg.as_string())

    server.quit()
    print('\nEmails enviados com sucesso!')

# Lista de endereços de e-mail dos destinatários
destinatarios = para

assunto = "Novo Teste de E-mail"
corpo = "Este é um exemplo de e-mail bonito e formatado utilizando HTML e CSS."
anexos = anexos

enviar_email(destinatarios, assunto, corpo, anexos)
