import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)  #587
    server.login('harshagullapudi99@gmail.com','ismx hdpn hbma tbhs')
    msg=EmailMessage()
    msg['FROM']='harshagullapudi99@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()