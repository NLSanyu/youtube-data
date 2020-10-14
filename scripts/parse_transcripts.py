import json

def parse_transcripts(transcripts):
    """
        Parses the transcripts from
        the transcripts.json file
        and saves them to a txt file
        named transcripts_text.txt
    """
    
    for transcript in transcripts:
        text = ''
        for part in transcript:
            
            print(transcript['text'])
            text = text + "\n" + transcript['text']
    print(text)

    save_text_to_file(text)
    
def save_text_to_file(text):
    f = open("data/transcripts_text.txt","a")
    f.write(text)
    f.close() 


if __name__ == '__main__':
    with open("data/transcripts.json", "r") as read_file:
        transcripts = json.load(read_file)
    parse_transcripts(transcripts)
