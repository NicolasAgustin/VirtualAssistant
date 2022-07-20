import pyttsx3
from pyttsx3.voice import Voice


class Speech:

    def __init__(this):
        # Init engine
        this._engine = pyttsx3.init()
        # Get the voice
        this._voice: Voice = next(iter(filter(
            lambda x: x.name == ('Microsoft Zira Desktop -'
                                 ' English (United States)'),
            this._engine.getProperty('voices')
        )), None)
        # Set rate
        this._engine.setProperty(
            'rate',
            this._engine.getProperty('rate')-50
        )
        # Set engine voice
        this._engine.setProperty('voice', this._voice.id)

    def say(this, text: str):
        this._engine.say(text)
        this._engine.runAndWait()
