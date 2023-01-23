from os import getcwd,listdir
from os.path import isfile,join,basename
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import schedule
import config


PORT = 465 
EMAIL_SERVER = "smtp.gmail.com"  # Adjust server address, if you are not using @outlook


# Read the variables for username and password from config.py
sender_email = config.username
password_email = config.password


def send_email(subject, receiver_email, attachments):
    # Create the base text message.
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["BCC"] = sender_email
    content =(f"""\
        Hi ,
        I hope you are well.

        Best regards
        David
        """
        )
    body = MIMEText(content, 'plain')
    msg.attach(body)
    
    filename = attachments
    with open(filename, 'r') as f:
        attachment = MIMEApplication(f.read(), Name=basename(filename))
        attachment['Content-Disposition'] = 'Attachment; filename= "{}"'.format(basename(filename))

    msg.attach(attachment)



    with smtplib.SMTP_SSL(EMAIL_SERVER, PORT) as server:
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())

def report_checking():
    dir_path = join(getcwd(),"report_files")
    files_list = [file for file in listdir(dir_path) if isfile(join(dir_path,file))]
    for file in files_list:
        with open(join(dir_path,file), 'r') as f:
            content = f.readlines()
            recipient_mail = content[0]
            mail_attachement = file
            mail_content = content[1]
            send_email(mail_content,recipient_mail,mail_attachement)
            f.close()

schedule.every().day.at("00:00").do(report_checking)