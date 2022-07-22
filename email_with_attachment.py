import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PIL import Image
import imghdr

sender = " "
receiver = " "
pwd = " "
sub = "Testing of Screen Logger prototype "
body = "This is a testing for sending mail with attachment in python"

msg=MIMEMultipart()
msg["From"]=sender
msg["To"]=receiver
msg["Body"]=body
msg["Subject"]=sub

msg.attach(MIMEText(body,_subtype="plain"))

images = ["one.png","two.png","three.png","four.png","five.png"]

'''with open("G:\\College Work\\SEMESTER - 2\\PYTHON LAB\\Package\\SCREEN_LOGGER\\new.pdf" , "rb") as fptr:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(fptr.read()) '''

for i in images:
    filename = i
    with open(i,'rb') as raw_img :
    #img  = MIMEBase(_maintype ="image", _subtype="PNG" , filename=i)
        img = raw_img.read()
        img_type = imghdr.what(raw_img.name)
        img_name = raw_img.name
        img.set_payload(Image.read())
        img.add_header("image","attachment",file_name=i)
        msg.attach(img)
        text=msg.as_string()
    

server = smtplib.SMTP("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login(sender,pwd)
server.sendmail(sender, receiver, text)
print("EMAILED SUCCUESSFULLY\n\n\n")
server.quit()


