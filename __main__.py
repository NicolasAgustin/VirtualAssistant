import pyaudio
from modules.speech import Speech
import speech_recognition as sr


def main():
    speech = Speech()
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            while True:
                print("Listening......")
                audio = r.listen(source)

                try:
                    print("Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    print(query)
                    speech.say(query)

                except Exception:
                    print("Did not catch that")
    except KeyboardInterrupt:
        speech.say('Goodbye')


if __name__ == '__main__':
    main()
