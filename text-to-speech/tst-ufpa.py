'''
BAIXE TODOS OS ARQUIVOS NECESSÁRIOS AQUI: "https://drive.google.com/drive/folders/1FjKBlwf4PAZjI4K76uPzQ4e1d8EgQZww?usp=sharing", inclui todos os arquivos mencionados abaixo.
--------------------------------------------------------------------------------------------------------------------------
Antes de começarmos, vamos precisar instalar algumas bibliotecas, caso você utilize linux você nao terá erros. Contudo, se você utiliza windows, tem uma seção de soluções de erros.
--------------------------------------------------------------------------------------------------------------------------
pip install SpeechRecognition pyaudio
--------------------------------------------------------------------------------------------------------------------------
pip install pocketsphinx
--------------------------------------------------------------------------------------------------------------------------
Em caso de erros (Windows):
1º - Desabilite seu firewall e anti virus durante a instalação.
2º - Instale: "https://sourceforge.net/projects/swig/files/swigwin/swigwin-3.0.12/swigwin-3.0.12.zip/download?use_mirror=ufpr", feito isso, descompacte no seguinte diretório: "C:\Program Files",
em seguida faça o seguinte procedimento: adicione o caminho da instalação as variveis de ambiente.
3º - Por ultimo instale: "Visual Studio 2015, Visual C++ 14.0", você pode conseguir por esse link:"http://www.microsoft.com/en-us/download/details.aspx?id=48145"
--------------------------------------------------------------------------------------------------------------------------
pip install pyttsx 
--------------------------------------------------------------------------------------------------------------------------
Em caso de erros (Windows):
1º - Baixe esse aquivo: "https://github.com/HashLDash/Site/blob/master/resources/PythonNaPratica/24-TTS/pyttsx.zip" depois abra o cmd como adm e de o seguinte comando "cd local_onde_o_aquivo_esta",
e depois "python setup.py".
--------------------------------------------------------------------------------------------------------------------------
pip install pypiwin32
--------------------------------------------------------------------------------------------------------------------------
pip install gtts
--------------------------------------------------------------------------------------------------------------------------
Instale: "https://sourceforge.net/projects/espeak/files/latest/download?source=typ_redirect"
--------------------------------------------------------------------------------------------------------------------------
'''
#RECONHECIMENTO DE VOZ
import speech_recognition as sr #importamos o modúlo

rec = sr.Recognizer() #instanciamos o modúlo do reconhecedor

with sr.Microphone() as fala: #chamos a gravação do microphone de fala
	frase = rec.listen(fala) #o metodo listen vai ouvir o que a gente falar e gravar na variavel frase

print(rec.recognize_google(frase, language='pt')) #transformando nossa fala em texto


#TRANSFORMANDO TEXTO EM FALA
import pyttsx # importamos o modúlo
en = pyttsx.init() # meotodo init seleciona um ending de sintetização, no caso o espeak
en.say("Hello, I am Ronan") # o metodo say para dizer o que queremos
en.say(Nice to meet you) 
en.runAndWait() # para ouvir o que foi escrito
en.setProperty('voice', b'brazil') # mudamos a propriedade setando pelo id para pt-br, o lemento b diz que a string está em bytes
en.say('Olá, tudo bem?')
en.runAndWait()

#TRANSFORMANDO TEXTO EM FALA - USANDO API DO GOOGLE
from gtts import gTTS # importamos o modúlo gTTS
voz = gTTS("Olá, tudo bem?", lang ="pt") # guardamos o nosso texto na variavel voz
voz.save("voz.mp3") #salvamos com o comando save em mp3

import subprocess as s #importamos o subprocess e renomeamos a s
s.call(['MPC-HC', 'voz.mp3']) #com o comando call roda nosso comando de voz no player escolhido.