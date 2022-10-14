import smtplib
import email.message

def send_email(body):
	msg = email.message.Message()
	msg['Subject'] = ""
	msg['From'] = "my_email@gmail.com"
	msg['To'] = "to@gmail.com"
	password = ""	# not the real password, gmail generates a password for this purpose
	msg.add_header('Content-Type', 'text')
	msg.set_payload(body)
	
	s = smtplib.SMTP('smtp.gmail.com: 587')
	s.starttls()
	# login
	s.login(msg['From'], password)
	s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
	print("email sent")

body = "message"
send_email(body)

