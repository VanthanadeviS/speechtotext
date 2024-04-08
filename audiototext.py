import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = "D:\ML\speechtotext\ENG_M.wav"

# Use the recognizer to listen to the audio file
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Convert speech to text using Google Speech Recognition
try:
    text = recognizer.recognize_google(audio_data)
    print("Recognized text:")
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
