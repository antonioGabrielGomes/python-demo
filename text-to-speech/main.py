import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 100) 
engine.setProperty('pitch', 0.8)  # Tom aumentado em 20%

for voice in voices:
    print(voice.id)
    if voice.id == 'brazil':
        engine.setProperty('voice', voice.id)
        engine.say('hhue')
        engine.save_to_file('o que é isso?', 'test.mp3')

# engine.say("I will speak this text")
engine.runAndWait()