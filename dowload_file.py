import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service
import os
import pandas as pd

CLIENT_SECRET = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPES)

file_id = '1WaymK35JtvGMsHtjck4EFJlFUSyPfz8r'
request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))

fh.seek(0)

with open(os.path.join('./arquivos', 'download.json'), 'wb') as file:
    file.write(fh.read())
    file.close()

df = pd.read_json('./arquivos/download.json')
df.to_excel('./arquivos/arquivo_drive.xlsx')
