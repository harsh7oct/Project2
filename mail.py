from smtplib import SMTP
fromaddr="harsh7oct@gmail.com"
toaddr="srkvkr@gmail.com"
message='''import smtplib
fromaddr="harsh7oct@gmail.com"
toaddr="srkvkr@gmail.com"
message="i am harsh"
password='onlyn2107@'
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, password)

server.sendmail(fromaddr, toaddr, message)
server.quit() '''

password='onlyn2107@'
server=SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, password)
server.sendmail(fromaddr, toaddr, message)
server.quit()