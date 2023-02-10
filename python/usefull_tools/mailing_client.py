import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()

password = ""	# remember to remove it!!!!!!!!!!!

server.login("alfredoncdossantos@gmail.com", password)

msg = MIMEMultipart()
msg["From"] = "Alfredo"
msg["To"] = "nelsontecnico6@gmail.com"	# remember to remove it!
msg["Subject"] = "testing with python"

message = "If you're reading this it means the script worked"
msg.attach(MIMEText(message, "plain"))
filename = "/home/alfredo/Desktop/Horus/livros/face.png"
attachment = open(filename, "rb")
p = MIMEBase("application", "octet-stream")
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f"attachment; filename={filename}")
msg.attach(p)
text = msg.as_string()
server.sendmail("alfredoncdossantos@gmail.com", "nelsontecnico6@gmail.com", text)

