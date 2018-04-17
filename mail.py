from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import smtplib
def mailer(imagename="20180414162441.jpg",path="E:\\CV2_Snaps\\20180414162441.jpg"):
# create message object instance
    msg = MIMEMultipart()
    filename = imagename
    attachment = open(path, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    sub = filename.split(".")
    message = "Thank you"
    # setup the parameters of the message
    password = "Guddi4321"
    msg['From'] = "soumyapatnaik2018@yahoo.com"
    msg['To'] = "soumyapatnaik2018@yahoo.com"
    msg['Subject'] = sub[0]
    # add in the message body
    #msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.mail.yahoo.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print ("successfully sent email to %s:" % (msg['To']))

if __name__ == '__main__':
    mailer()