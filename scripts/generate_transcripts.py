import json
from youtube_transcript_api import YouTubeTranscriptApi


def transcribe(video_ids):
    transcript_list = []
    for video in videos:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video['video_id'])
            transcript_list.append(transcript)
            print(transcript)
        except RuntimeError as error:
            print(error)
        finally:
            print('Transcript error')

    with open("data/transcripts.json", "w") as outfile:
        json.dump(transcript_list, outfile)


if __name__ == '__main__':
    with open("data/videos.json", "r") as read_file:
        videos = json.load(read_file)
    transcribe(videos)
