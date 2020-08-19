from decouple import config
from googleapiclient.discovery import build

api_key = config('API_KEY')
service = build('youtube', 'v3', developerKey=api_key)

request = service.channels().list(
    part='statistics',
    forUsername='ntvuganda'
)

response = request.execute()
print(response)
