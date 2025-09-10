import speech_recognition as sr
import pyttsx3
import requests
listener = sr.Recognizer()
speaker = pyttsx3.init()

speaker.setProperty('rate', 100)

def speak(text):
    print("Assistant:", text)
    speaker.say(text)
    speaker.runAndWait()

name = "tom"
speak("I am your " + name + ". Tell me boss.")

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)

            if name in command:
                command = command.replace(name, "").strip()
                return command
            return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your voice.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

while True:
    user = take_command()
    if user is None:
        continue

    if "close" in user:
        speak("See you again. I will be there anytime for you.")
        break

    elif "weather" in user:
        city = "vizag"
        api_key = "56dc960ae2a6bf973fd5a3b998773b82"
        url = f"https://api.openweathermap.org/data/2.5/weather?weather?q={city}&appid={api_key}"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            speak(f"The weather in {city} is {weather} with {temp} degrees Celsius.")
        else:
            speak("Sorry, I can't fetch the weather right now.")
