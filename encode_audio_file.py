import base64


def encode_audio(audio):
    audio_content = audio.read()
    return base64.b64encode(audio_content)


if __name__ == '__main__':
    audio_file = '/speech_to_text_snippet.wav'
    encode_audio(audio_file)
