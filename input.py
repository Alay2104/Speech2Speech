import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Capture voice
            text = recognizer.recognize_google(audio)  # Convert speech to text
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Could not request results from Google API.")
        except sr.WaitTimeoutError:
            print("Listening timed out. Try speaking again.")
        return None

def translate_text(text, target_lang="es"):  # Default translation to Spanish
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    print(f"Translated ({target_lang}): {translated.text}")
    return translated.text

def text_to_speech(text, lang="es"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save("translated_audio.mp3")
    # windows os.system("start translated_audio.mp3")
    os.system("afplay translated_audio.mp3") #mac
    #Linux: os.system("mpg321 translated_audio.mp3")

def get_target_language():
    languages = {
        "Spanish": "es", "French": "fr", "German": "de",
        "Hindi": "hi", "Chinese": "zh-cn", "Japanese": "ja",
        "Arabic": "ar", "Russian": "ru", "Portuguese": "pt"
    }

    print("\nAvailable Languages:")
    for lang, code in languages.items():
        print(f"- {lang} ({code})")

    choice = input("\nEnter target language (e.g., 'French', 'Spanish'): ").strip().title()

    return languages.get(choice, "hi")  # Default to hindi if invalid


if __name__ == "__main__":
    target_lang = get_target_language()  # Ask user for language
    text = capture_voice()
    if text:
        translated_text = translate_text(text, target_lang)
        text_to_speech(translated_text, target_lang)
