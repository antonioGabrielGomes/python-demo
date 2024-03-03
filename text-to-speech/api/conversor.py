from gtts import gTTS

def text_to_audio(text: ''):
    if text != '':
        audio = gTTS(f"{text}", lang ="pt")
        audio.save('public/exemplo.mp3')
        return audio
    else:
        return False


# https://github.com/nateshmbhat/pyttsx3
# https://gtts.readthedocs.io/en/latest/
# https://cloud.google.com/text-to-speech/