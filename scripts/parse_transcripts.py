import json

def parse_transcripts(transcripts):
    """
        Parses the transcripts from
        the transcripts.json file
        and saves them to a txt file
        named transcripts_text.txt
    """
    all_text_list = []
    for transcript in transcripts:
        text_list = [f"Title: {transcript[-1]['title']}"]
        for part in transcript:
            text_list.append(part.get('text', ' '))
            text = "\n".join(text_list)
        all_text_list.append(text)
    all_text = "\n".join(all_text_list)
    save_text_to_file(all_text)
    
def save_text_to_file(text):
    f = open("data/transcripts_text.txt","a")
    f.write(text)
    f.close() 


if __name__ == '__main__':
    with open("data/transcripts.json", "r") as read_file:
        transcripts = json.load(read_file)
    parse_transcripts(transcripts)
