""" import speech_recognition as sr

def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio file

    try:
        print("Transcribing audio...")
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))

if __name__ == "__main__":
    audio_file = "untitled.wav"  # Update this with the path to your audio file
    convert_audio_to_text(audio_file) """

import speech_recognition as sr
import openai

def convert_audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the audio file

    try:
        print("Transcribing audio...")
        text = recognizer.recognize_google(audio_data)
        print("Transcription:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
        return None

def ask_gpt(question):
    client = openai.OpenAI(api_key="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")
    assistant = client.beta.assistants.create(
        name="Scam Predictor",
        instructions="You are predicting whether the message is from a scammer or not. The text provided to you is the text from a random phone number. Based off its contents, you are to determine if it has scam intent or not. Simply respond yes or no. Here are common themes seen in scam calls. The caller is mentioning insurance, warranty, social security, bank information, or any other important information sometimes with urgency.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-3.5-turbo"
    )
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="Hi my name is John Doe, I am calling you regarding your auto warranty expiration."
    )
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
    )
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    for message in reversed(messages.data):
        print(message.role + ": " + message.content[0].text.value)

if __name__ == "__main__":
    audio_file = "untitled.wav"  # Update this with the path to your audio file
    question = convert_audio_to_text(audio_file)
    
    ask_gpt(question)
