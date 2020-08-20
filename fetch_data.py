from decouple import config
from googleapiclient.discovery import build

api_key = config('API_KEY')
service = build('youtube', 'v3', developerKey=api_key)

channels_request = service.channels().list(
    part='id, contentDetails',
    forUsername='ntvuganda'
)

video_ids = []

channels_response = channels_request.execute()
for channel in channels_response['items']:
    uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']

    next_page_token = None
    while next_page_token != '':
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

        # next_page_token = playlistitems_response['nextPageToken']
        next_page_token = ''   # replace with above line after testing

sample_video_id = video_ids[0]['video_id']
captions_request = service.captions().list(
    part='id, snippet',
    videoId=sample_video_id
)
captions_response = captions_request.execute()
print(captions_response)

# for caption in captions_response['items']:
#     caption_id = caption['id']
#     caption_download = service.captions().download(
#         id=caption_id
#     ).execute()

#     print(caption_download)
