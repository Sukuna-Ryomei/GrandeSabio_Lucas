import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Grande Sábio está ouvindo...")
    audio = recognizer.listen(source)

try:
    texto = recognizer.recognize_google(audio, language="pt-BR")
    print("Você disse:", texto)

except sr.UnknownValueError:
    print("Não consegui entender o que você disse.")

except sr.RequestError as erro:
    print("Erro ao conectar ao serviço de reconhecimento:", erro)