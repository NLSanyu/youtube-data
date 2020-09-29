from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'WTzwIqaM7qU'
transcript = YouTubeTranscriptApi.get_transcript(video_id)
print(transcript)
