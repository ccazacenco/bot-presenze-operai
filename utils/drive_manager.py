from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
from config import Config
import os

class DriveManager:
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/drive']
        self.creds = Credentials.from_service_account_file(
            Config.GOOGLE_CREDS_PATH, 
            scopes=self.scope
        )
        self.service = build('drive', 'v3', credentials=self.creds)

    def upload_file(self, file_path, folder_id):
        file_metadata = {
            'name': os.path.basename(file_path),
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path)
        file = self.service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id,webViewLink'
        ).execute()
        
        self.service.permissions().create(
            fileId=file['id'],
            body={'type': 'anyone', 'role': 'reader'},
            fields='id'
        ).execute()
        return file['webViewLink']
