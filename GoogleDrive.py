# Google drive backup

# Upload files to google drive
# List files in google drive
# Download files from google drive

# pip install pydrive

import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import pyshorteners


def grant_access(folder, emails, role='writer'):
    for email in emails:
        permission = folder.InsertPermission({
            'type': 'user',
            'value': email,
            'role': role,
        })
    return permission
    

def Upload_in_GoogleDrive():
    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    root_folder_id = '14LzXvFZUp05MHsPK-96dG09YxQk6uNm8'

    current_date = datetime.now().strftime("%d-%m-%Y")
    new_folder_name = "UserExtract_" + current_date
    new_folder = drive.CreateFile({'title': new_folder_name, 'parents': [{'id': root_folder_id}], 'mimeType': 'application/vnd.google-apps.folder'})
    new_folder.Upload()
    new_folder_id = new_folder['id']
    Folder_Link = new_folder['alternateLink']

    s = pyshorteners.Shortener()
    f_link = s.tinyurl.short(Folder_Link)

    # Upload files
    directory = "C:/Users/0175305/Downloads/12thFeb2024"
    for f in os.listdir(directory):
        filename = os.path.join(directory, f)
        gfile = drive.CreateFile({'parents' : [{'id' : new_folder_id}], 'title' : f})
        gfile.SetContentFile(filename)
        gfile.Upload()


    print('Files are uploaded successfully')

    user_emails = ['mohammed.zuber@averydennison.com','sudini.reddy@averydennison.com','rohitha.duppi@averydennison.com']
    grant_access(drive.CreateFile({'id': new_folder_id}), user_emails)

    print(f_link)
    return f_link



if __name__ == "__main__":
    Upload_in_GoogleDrive()

    
 