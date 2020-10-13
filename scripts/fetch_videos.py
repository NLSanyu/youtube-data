from decouple import config
from googleapiclient.discovery import build
import json

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
api_key = config('API_KEY')
service = build(API_SERVICE_NAME, API_VERSION, developerKey=api_key)


def get_channels_from_file():
    """
        Retrieves channel names of the channels 
        whose video transcripts we want to fetch,
        from the channels.json file
    """
    with open("data/channels.json", "r") as read_file:
        channels = json.load(read_file)

    return channels


def fetch_videos():
    """
        Fetches the video title and video id
        of each video uploaded by the channels
        in our channels.json file
    """
    channels = get_channels_from_file()

    channels_request = service.channels().list(
        part='id, contentDetails',
        forUsername=channels[0]['channelUsername']  # first channel for now
    )

    video_list = []

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
                video_list.append({'title': title, 'video_id': video_id})

            next_page_token = playlistitems_response.get('nextPageToken')

    return video_list


if __name__ == '__main__':
    video_list = fetch_videos()
    with open("data/videos.json", "w") as outfile:
        json.dump(video_list, outfile)