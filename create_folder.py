from Google import Create_Service

CLIENT_SECRET = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET, API_NAME, API_VERSION, SCOPES)

folder = {'name': 'beAnalytic',
          'mimeType': 'application/vnd.google-apps.folder'}

drive_service.files().create(body=folder).execute()
