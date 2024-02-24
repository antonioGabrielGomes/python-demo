from gtts import gTTS # importamos o modúlo gTTS
voz = gTTS(f"5 + 5 é igual a {5+5}", lang ="pt") # guardamos o nosso texto na variavel voz
voz.save("voz.mp3") #salvamos com o comando save em mp3

import subprocess as s #importamos o subprocess e renomeamos a s
s.call(['MPC-HC', 'voz.mp3'])