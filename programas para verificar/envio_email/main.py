import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Classe para enviar email
class EmailAut:
    def __init__(self, destinatario, assunto, conteudo):
        self.destinatario = destinatario  # Corrigido o nome da variável
        self.assunto = assunto
        self.conteudo = conteudo

    def envio(self):
        msg = MIMEMultipart()
        msg.add_header("Content-Type", "text/html")

        msg["From"] = "seu_email@gmail.com"  # Seu e-mail
        password = "senha_do_seu_email"  # Sua senha

        msg["Subject"] = self.assunto
        msg["To"] = self.destinatario
        msg.attach(MIMEText(self.conteudo, "plain"))

        # Configuração do servidor SMTP
        s = smtplib.SMTP("smtp.gmail.com", 587)  # Corrigido para "smtp.gmail.com"
        s.starttls()  # Inicia a comunicação TLS
        s.login(msg["From"], password)  # Corrigido o argumento

        # Envia o e-mail
        s.sendmail(msg["From"], msg["To"], msg.as_string().encode("utf-8"))
        s.quit()

        print(f"E-mail enviado para {self.destinatario}.")

if __name__ == "__main__":
    enviando = EmailAut(
        destinatario="email_destinatario@servidor.com",  # Destinatário
        assunto="Assunto que deseja tratar no e-mail",  # Assunto do e-mail
        conteudo="Texto que deseja colocar no corpo do email"  # Corpo do e-mail
    )
    
    enviando.envio()