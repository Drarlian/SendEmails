import smtplib  # -> Biblioteca padrão do Python que define um cliente SMTP para enviar e-mails.
from email.mime.multipart import MIMEMultipart  # -> Classe usada para criar um e-mail que pode ter diferentes partes (por exemplo, texto e anexos).
from email.mime.text import MIMEText  # -> Classe usada para criar uma parte de texto simples do e-mail.

with open('informations.txt', 'r') as infos:
    new_infos = infos.readlines()
    infos_emails = new_infos[0].replace('\n', '').split('=')[1]
    infos_senha = new_infos[1].split('=')[1]
    infos_destino = new_infos[2].split('=')[1]

# Configurações do servidor de e-mail
smtp_server = "smtp.gmail.com"  # -> Endereço do servidor SMTP do Gmail.
smtp_port = 587  # -> Porta do servidor SMTP. O valor 587 é usado para conexões com STARTTLS.
email = infos_emails  # -> Seu endereço de e-mail do Gmail.
password = infos_senha  # -> A senha de aplicativo.

# Configuração do e-mail
msg = MIMEMultipart()  # -> Cria uma instância de um e-mail multipart, permitindo adicionar múltiplas partes (como texto e anexos).
msg['From'] = email  # -> Define o remetente do e-mail.
msg['To'] = infos_destino  # -> Define o destinatário do e-mail.
msg['Subject'] = "Assunto do Email!"  # -> Define o assunto do e-mail.

# Corpo do e-mail (Texto)
# corpo = "Este e-mail está sendo enviado para informar que o forno está em temperatura alarmante"  # -> Define o texto do corpo do e-mail.
# msg.attach(MIMEText(corpo, 'plain'))  # -> Anexa o corpo do e-mail como texto simples ao e-mail multipart.

# Corpo do e-mail (HTML)
corpo_html = """
<html>
<head></head>
<body>
    <h1>Este é um e-mail enviado através do Python</h1>
    <p>Este e-mail contém <b>HTML</b>!</p>
</body>
</html>
"""  # -> Define o conteúdo do corpo do e-mail.
msg.attach(MIMEText(corpo_html, 'html'))  # -> Anexa o corpo do e-mail como html ao e-mail multipart.

try:
    # Conectando ao servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)  # -> Cria uma instância do servidor SMTP e conecta ao servidor SMTP do Gmail usando o endereço e a porta especificados.
    server.starttls()  # -> Inicia a conexão TLS (Transport Layer Security), que criptografa a conexão.

    # Fazendo login no servidor SMTP
    server.login(email, password)  # -> Faz login no servidor SMTP usando seu endereço de e-mail e a senha de aplicativo.

    # Enviando o e-mail
    server.sendmail(email, msg['To'], msg.as_string())  # -> Envia o e-mail do remetente para o destinatário. O método msg.as_string() converte o objeto do e-mail em uma string formatada adequadamente.
    print("E-mail enviado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

else:
    server.quit()
