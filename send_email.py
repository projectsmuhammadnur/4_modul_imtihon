from emailtrainrs import text1, text2
import smtplib
from email.message import EmailMessage

password = text1
sender = text2
server = "smtp.gmail.com"
port = 465
msg = EmailMessage()
msg["From"] = sender
msg["Subject"] = "Suxbatullayev Muhammad Nur 4-modul imtihon"
msg.add_alternative("""
<!DOCTYPE html>
<html lang="en">
<body>
    <h1 style="color: Red"; text-align: center>Docker image: docker pull muhammadnur/exam_p13_bot:alpine</h1>
    <h2 style="color: Blue"; text-align: center>docker-compose.yml githubda bor</h2>
    <h1 style="color: Red"; text-align: center>Github project: https://github.com/projectsmuhammadnur/4_modul_imtihon.git</h1>
</body>
</html>
""", subtype="html")
msg['To'] = "absaitovdev@gmail.com"
with smtplib.SMTP_SSL(server, port) as server:
    server.login(sender, password)
    server.send_message(msg)
