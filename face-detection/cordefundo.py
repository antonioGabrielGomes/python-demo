def determinar_cor_fundo(imagem, x, y, w, h):
    print(image)
    regiao = imagem #[y-20:y+h+20, x-20:x+w+20]
    
    regiao_gray = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(f"result-{random()}-test.png", regiao_gray)
    
    media_intensidade = regiao_gray.mean()
    
    limite = 100
    
    # Comparar com o limite
    if media_intensidade < limite:
        print("Fundo Escuro")
    else:
        print("Fundo Claro")
    


'''
## 
* fundo claro
* permitido utilizar apenas arquivo de foto com extensão .jpg 
* os celulares possuem modo Embelezamento nativo de fábrica, portanto não utilize esse tipo de foto ou qualquer outro arquivo que foi previamente editado/tratado por um software
* outras:
 Facial ativado: Habilita/desabilita o reconhecimento facial no XPE;
» Aprendizado offline ativado: é um aperfeiçoamento do algoritmo de reconhecimento das faces cadas-
tradas, onde a cada novo acesso, ele realiza um aprendizado e melhora a detecção para futuros acessos;
» Envio automático erros e falhas (facial): debug para desenvolvimento e manutenção, com esses
dados a área técnica de suporte da Intelbras poderá analisar melhor as possíveis falhas para identificar
problemas (padrão de fábrica = desabilitado);
» Nível de similaridade da face: nível de semelhança entre faces;
Importante: em caso de cenários com usuários gêmeos univitelinos utilize o nível de similaridade da face
no Máximo conforme imagem abaixo;
» Nível de vivavicidade (anti-fake): o anti-fake garante que o equipamento não faça a liberação caso
seja mostrado a foto de um rosto, seja ela impressa ou digital. Com a função habilitada somente quando
a pessoa estiver em frente ao dispositivo será feito o reconhecimento. É possível utilizar quatro níveis de
anti-fake Baixo, Normal, Alto ou Máximo;
» Intervalo de reconhecimento (seg): é o intervalo de tempo entre acionamentos através de faces
válidas (Padrão de fábrica: 2 seg.);
Exemplo: ao detectar uma face e realizar o acionamento, o XPE aguardará o tempo configurado para realizar
uma nova validação de face e novo acionamento
- Intervalo sem detecção (seg): é o intervalo de tempo máximo em que o XPE tenta validar uma face não
reconhecida. Porém, assim que validada, o equipamento informará o resultado, não necessitando aguardar
o tempo configurado (Padrão de fábrica: 1 seg.)

Detecção de máscara: é possível habilitar o sistema para detectar máscaras e gerar alerta visual no
display ou bloqueio quando as pessoas não as estiverem usando;
» Desabilitado: desabilita a função;
» Uso de máscara obrigatório: se habilitado, o acesso de pessoas sem mascaras será negado. Também
não será possível realizar o acionamento da saída através de chaveiros e senhas e nem realizar cha-
madas do XPE (as tecla
ser detectado).
'''