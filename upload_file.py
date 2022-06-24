from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPES)

folder_id = '1-XDCkK5hEPqc489_q5RWJGmdfF9LJ12a'

file_name = 'arquivo_drive.xlsx'

file_info = {'name': file_name,
             'parents': [folder_id]}

file = MediaFileUpload('./arquivos/arquivo_drive.xlsx',
                       mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

drive_service.files().create(body=file_info, media_body=file, fields='id').execute()
