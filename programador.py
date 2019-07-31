#
import speech_recognition as sr
import subprocess 

rec = sr.Recognizer()
sair =['Sair', 'ate mais', 'sair']
tarefa =['tarefa', 'pc', 'PC']
abrir =['abrir', 'abra', 'veja']
navegador =['youtube', 'YouTube', 'google', 'tradutor']
mostra =['print', 'mostra', 'mostra na tela']
escreve_arquivo = ''
controle_escreve = 0

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

        # Escreve print na tela __________________
        if controle_escreve == 1:
            escreve_arquivo = resposta + "\')"
            arquivo.write(escreve_arquivo)
            controle_escreve = -1
            
        if resposta in mostra:
            print('print:', end='')
            
            arquivo = open('programa.py', 'w')
            escreve_arquivo = "print(\'"
            arquivo.write(escreve_arquivo)
            controle_escreve = 1
        
       
