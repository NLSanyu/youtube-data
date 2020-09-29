from decouple import config
from googleapiclient.discovery import build

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
api_key = config('API_KEY')
service = build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)

channels_request = service.channels().list(
    part='id, contentDetails',
    forUsername='ntvuganda'
)

video_ids = []

channels_response = channels_request.execute()
for channel in channels_response['items']:
    uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']

    next_page_token = ''
    while next_page_token is not None:
        playlistitems_response = service.playlistItems().list(
            playlistId=uploads_list_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for playlist_item in playlistitems_response['items']:
            title = playlist_item['snippet']['title']
            video_id = playlist_item['snippet']['resourceId']['videoId']
            print(f'{title}, {video_id}')
            video_ids.append({'title': title, 'video_id': video_id})

        # next_page_token = playlistitems_response.get('nextPageToken')
        next_page_token = ''   # replace with above line after testing
