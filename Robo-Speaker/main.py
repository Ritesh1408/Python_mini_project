import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.01")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "0":
            engine.say("Bye Bye Dear")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
