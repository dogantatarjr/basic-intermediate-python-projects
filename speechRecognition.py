import speech_recognition

recognizer = speech_recognition.Recognizer()

while True:
    print("Dinliyor...")

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language='tr-tr')
            text = text.lower()

            print(f"Dinlenen Metin: {text}")

    except speech_recognition.UnknownValueError():
        recognizer = speech_recognition.Recognizer()
        continue