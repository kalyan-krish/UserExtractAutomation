#https://www.youtube.com/watch?v=g_j6ILT-X0k

#from email.MIMEMultipart import MIMEMultipart
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from GoogleDrive import Upload_in_GoogleDrive
from datetime import datetime



def send_email():
    email_sender = 'ramachandruni.kalyan@averydennison.com'

    email_password = 'bxhbpmqkxyfxghbf'

    email_receivers = ['mohammed.zuber@averydennison.com','sudini.reddy@averydennison.com','rohitha.duppi@averydennison.com']

    subject = 'PriceFx User Extracts for' + datetime.now().strftime('%d-%M-%Y')

    FolderLink = Upload_in_GoogleDrive()



    msg = MIMEText(f""" 
                   
                    Hello Team,

                    Please find the user extracts in below link, the user information from Price FX till 12th February 2024.
                   
                    {FolderLink}

                    Thanks & Regards,
                    R.Sai Kalyan 
                   """)

    msg['From'] = email_sender
    msg['To'] = ",".join(email_receivers)
    msg['Subject'] = subject


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receivers,msg.as_string())




if __name__ == "__main__":
    send_email()
