#Rieconhece a voz e escreve os comandos em um arquivo 
# teste no Gitkraken
import speech_recognition as sr
import subprocess 

rec = sr.Recognizer()
sair =['Sair', 'ate mais', 'sair']
tarefa =['tarefa', 'pc', 'PC']
abrir =['abrir', 'abra', 'veja']
navegador =['youtube', 'YouTube', 'google', 'tradutor']
mostra =['print', 'mostra', 'mostra na tela']
variavel =['variável', 'var']
abrir_arquivo =['abrir arquivo', 'abrir programa', 'criar programa']
escreve_arquivo = ''
nome_var = ''
controle_mostra = controle_variavel = valor_variavel = cotrole_abre_arqui = controle_nome_var = controle_valor_var = 0


def falaRobo():
    print('🤖: ', end='')

def escreve(palavra):
    print('Escrevento...')
    arquivo.write(palavra)

while True:
    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)
        audio = rec.listen(s)
        print('🎙:', end='')
        resposta = rec.recognize_google(audio, language='pt')
        print(resposta)

        # Abrir arquivo _____________________
        if cotrole_abre_arqui == 1:
            arquivo = 'script robo/' + resposta + '.py'
            arquivo = open(arquivo, 'w')
            cotrole_abre_arqui = 0

        if resposta in abrir_arquivo:
            falaRobo()
            print('Nome do arquivo?')
            cotrole_abre_arqui = 1

        if resposta in sair:
            print('Ate mais :)')
            arquivo.close()
            break

        # Escreve print na tela __________________
        if controle_mostra == 1:
            print('print(', escreve_arquivo, ')')
            escreve_arquivo = escreve_arquivo + resposta + "\')"
            escreve(escreve_arquivo)
            #arquivo.write(escreve_arquivo)
            controle_escreve = 0
            
            
        if resposta in mostra:
            print('print:', end='')
            #arquivo = open('programa.py', 'w+')
            escreve_arquivo = "print(\'"
            controle_mostra = 1
        
        # Variavel _______________________________
        if controle_variavel == 1:
            print('Nome da variavel? ', end='')
            nome_var = resposta
            controle_variavel = 0
            valor_variavel = 1

        if valor_variavel == 1:
            falaRobo()
            print('Qual é o valor? ', resposta)
            valor_var = resposta
            print('Variavel:', nome_var, '=', valor_var)
            valor_variavel = 0
            controle_nome_var = 1
        
        if controle_valor_var == 1:
            nome_var = nome_var + '=' + valor_var
            escreve(nome_var)
            controle_valor_var = 0

        if resposta in variavel:
            falaRobo()
            print('Nome variavel?', end='')
            controle_variavel = 1

       
           
        
