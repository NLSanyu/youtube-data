import json
from youtube_transcript_api import YouTubeTranscriptApi


def get_transcripts(videos):
    """
        Fetches the transcripts of each video 
        in the videos.json file
    """
    transcript_list = []
    for video in videos:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video['video_id'])
            transcript.append({'title': video['title']})
            transcript_list.append(transcript)
            print(transcript)            
        except Exception:
            pass

    create_transcripts_file(transcript_list)

def create_transcripts_file(transcript_list):
    """
        Creates a transcripts.json file (in the /data folder) 
        from the transcript_list array.
    """
    with open("data/transcripts.json", "w") as outfile:
        json.dump(transcript_list, outfile)



if __name__ == '__main__':
    with open("data/videos.json", "r") as read_file:
        videos = json.load(read_file)
    get_transcripts(videos[:5]) # sample of first 5 videos
