from google.cloud import speech

def speech_to_text(
    config: speech.RecognitionConfig,
    audio: speech.RecognitionAudio,) -> speech.RecognizeResponse:

    client = speech.SpeechClient()

    # Synchronous speech recognition request
    response = client.recognize(config=config, audio=audio)
    print(response)
    print_response(response)
    return response


def print_response(response: speech.RecognizeResponse):
    for result in response.results:
        print_result(result)


def print_result(result: speech.SpeechRecognitionResult):
    best_alternative = result.alternatives[0]
    print("-" * 80)
    print(f"language_code: {result.language_code}")
    print(f"transcript:    {best_alternative.transcript}")
    print(f"confidence:    {best_alternative.confidence:.0%}")


if __name__ == '__main__':
    config = speech.RecognitionConfig(
        language_code="es-US",
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=48000
    )

    print("Opening file")
    with open('spanish-test.mp3', 'rb') as file:
        c = file.read()

    audio = speech.RecognitionAudio(
        content = c,
    )
    print("Converting speech to text")
    
    response = speech_to_text(config, audio)