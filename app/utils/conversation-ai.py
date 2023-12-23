from google.cloud import speech

def audio_to_text(audio: speech.RecognitionAudio, config: speech.RecognitionConfig) -> speech.RecognizeResponse:
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    return response

def generate_response(input):
    pass



if __name__ == '__main__':
    cont = None
    config = speech.RecognitionConfig()
    audio = speech.RecognitionAudio(content=cont)