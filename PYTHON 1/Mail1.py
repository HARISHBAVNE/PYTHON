import smtplib
from email.message import EmailMessage 


Mail = EmailMessage()
Mail['subject'] = "Automated analysis of Process running on system"
Mail ['from']    = "Harish"
Mail ['To']  = "harishbavne@gmail.com"

Mail.set_content("Hello, This is automated mail")

with open("msg.txt") as message:
    data = message.read()
    Mail.set_content(data)

with open("msg.txt",'rb') as fd:
    data = fd.read()
    FileName = fd.name
    Mail.add_attachment(data,maintype = "Application",subtype = "txt",filename = FileName)
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("harishbavne@gmail.com","Chitraharish")

server.send_message(Mail)



server.quit()

print("Mail sent")
