import speech_recognition as sr
import subprocess 

rec = sr.Recognizer()
sair =['Sair', 'ate mais', 'sair']
tarefa =['tarefa', 'pc', 'PC']
abrir =['abrir', 'abra', 'veja']
navegador =['youtube', 'YouTube', 'google', 'tradutor']

while True:
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        print('teste de som!')
        audio = rec.listen(s)

        resposta = rec.recognize_google(audio, language='pt')

        print('Resposta:', resposta)

        if resposta in sair:
            print('Ate mais :)')
            break
        
        if resposta in tarefa:
            print('Qual tarefa?')

        if resposta in abrir:
            print('Fala !')
            resposta = rec.recognize_google(audio, language='pt')
            link = 'http://www.' + resposta + '.com'
            subprocess.Popen(['xdg-open', resposta])
            #subprocess.Popen(['xdg-open', 'http://www.youtube.com'])

        if resposta in navegador:
            print('Navegar!')
            #link = resposta.()
            link = 'http://www.' + resposta + '.com'
            subprocess.Popen(['xdg-open', resposta])
            
            
            # fadsfadsf