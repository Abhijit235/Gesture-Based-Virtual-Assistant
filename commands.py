import webbrowser
import pyttsx3

engine = pyttsx3.init()

def perform_action(fingers):
    if fingers == 1:
        engine.say("Opening YouTube")
        engine.runAndWait()
        webbrowser.open("https://youtube.com")
    elif fingers == 2:
        engine.say("Showing the weather")
        engine.runAndWait()
        webbrowser.open("https://www.weather.com")
    elif fingers == 3:
        engine.say("Playing music")
        engine.runAndWait()
        webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    elif fingers == 5:
        engine.say("Hello, I am your gesture assistant!")
        engine.runAndWait()
    else:
        engine.say("Gesture not recognized")
        engine.runAndWait()
