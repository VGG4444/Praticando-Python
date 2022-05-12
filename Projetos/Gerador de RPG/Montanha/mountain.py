from random import randint


def descricao(um, dois, tres, quatro):
    descricaoP = [[
                      '1 O horizonte é impedido pelas paredes assimétricas de pedregulhos e rochas, formando um pequeno caminho quase certo pelo percurso. A pouca vegetação, os pinheiros e o resto das árvores coníferas permanecem nos lugares mais altos, mas a grama comum também surge em um canto ou outro'],
                  [
                      '2 A altitude  deixa as pedras escorregadias e lisas, fazendo a visão quase paralela, e às vezes de cima, das nuvens ser comum. A folhagem resistente é típica aqui, já que o ar começa a ficar rarefeito e os paredões não cessam'],
                  [
                      '3 As rochas irregulares frequentemente fazem formas contraídas dentro da montanha, o que resulta em vários possíveis lares de criaturas menores e ninhos de aves. Em grande parte do caminho, de longe, é possível ver a paisagem distante e baixa dos arredores de um lado.'],
                  [
                      '4 Barrancos e precipícios podem ser vistos em todos os pontos da região, o que torna o terreno acidentado e perigoso. Valas com restos mortais de animais e humanoides são comuns, assim como a legião de aves que rotacionam no céu antes de descer à presa'],
                  [
                      '5 As pedras escuras são dominantes aqui, um terreno íngreme faz parte do habitual e a pouca vegetação só é vista em raros lugares ao longe. No entanto, a terra umedecida ainda pode ser encontrada'],
                  [
                      '6 A grande altitude faz com neve comece a surgir no local, tanto nos picos mais altos (ao menos aqueles que não estão escondidos pela neblina) como nas pedras e no chão mais baixo. A neve é fina e escassa, mas a atmosfera fria esfria o pouco ar que entra pelos pulmões']]
    descricaoS = [['1-2 Sussurros e sopros do vento gélido'],
                  ['1-2 Sussurros e sopros do vento gélido'],
                  ['3 O som distante das poucas aves que não se escondem e voam muito alto'],
                  ['4-5 Apenas o som dos passos, respirações ofegantes e impacto contra pedras'],
                  ['4-5 Apenas o som dos passos, respirações ofegantes e impacto contra pedras'],
                  ['6 O vento uiva alto por entre as pedras e seus vãos apertados']]
    descricaoO = [['1 Cheiro distante e fraco de chuva'],
                  ['2 Cheiro de terra molhada'],
                  ['3 Cheiro forte de chuva'],
                  ['4 Cheiro de algo apodrecendo'],
                  ['5 Cheiro de carvão e/ou minérios'],
                  ['6 Cheiro forte da vegetação local']]
    descricaoC = [['1 Ventos fortes e gélidos balançam os cabelos e roupas, hora ou outra fazendo os ossos tremerem'],
                  ['2 A grande altitude e a falta de ar chegam a confundir os sentidos'],
                  ['3 Alguns montes e pedras são cobertos por uma fina camada de neve'],
                  ['4 A súbita descida faz a respiração habitual voltar ao normal'],
                  ['5 As passadas parecem mais pesadas nessa parte da montanha, a fadiga das pernas começa a surgir'],
                  ['6 Alguns galhos secos e terra firme e plana surgem na paisagem']]

    rUm = descricaoP[um]
    rDois = descricaoS[dois]
    rTres = descricaoO[tres]
    rQuatro = descricaoC[quatro]
    return rUm, rDois, rTres, rQuatro


def assentamento():
    global assent, ocupante, ocupacao, especi, especii
    tipoassent = randint(1, 20)
    if tipoassent < 11:
        assent = "1-10 Lugarejo"
    if 10 < tipoassent < 15:
        assent = "11-14	Povoado"
    if 14 < tipoassent < 17:
        assent = "15-16	Aldeia"
    if 16 < tipoassent:
        assent = "17-20	Acampamento com assentamento improvisado (Role um encontro com humanoides)"

    tipoocupante = randint(1, 20)
    if tipoocupante < 11:
        ocupante = "1-10 Anão (Assentamento dentro da montanha/caverna)"
    if 10 < tipoocupante < 14:
        ocupante = "11-13 Aarakocra"
    if 13 < tipoocupante < 15:
        ocupante = "14 Kobolds"
    if 14 < tipoocupante < 16:
        ocupante = "15 Orcs e Gigantes (Ogros, Ettins, etc)"
    if 15 < tipoocupante < 21:
        tabelaocup = randint(1, 20)
        if tabelaocup == 1:
            ocupante = "1 Humano"
        if 1 < tabelaocup < 5:
            ocupante = "2-4 Elfo"
        if 4 < tabelaocup < 7:
            ocupante = "5-6 Gnomo"
        if 6 < tabelaocup < 9:
            ocupante = "7-8 Halfling"
        if 8 < tabelaocup < 12:
            ocupante = "9-11 Goliath"
        if 11 < tabelaocup < 14:
            ocupante = "12-13 Tiefling"
        if 13 < tabelaocup < 15:
            ocupante = "Role duas vezes"
        if 15 < tabelaocup < 21:
            exotico = randint(1, 20)
            if 0 < exotico < 5:
                ocupante = "1-4 Goblin"
            if 4 < exotico < 6:
                ocupante = "5 Hobgoblin"
            if 5 < exotico < 8:
                ocupante = "6-7 Tabaxi"
            if 7 < exotico < 9:
                ocupante = "8 Thri-Keen"
            if 8 < exotico < 11:
                ocupante = "9-10 Draconato"
            if 10 < exotico < 12:
                ocupante = "11 Kenku"
            if 11 < exotico < 13:
                ocupante = "12 Minotauro"
            if 12 < exotico < 15:
                ocupante = "13-14 Centauros	"
            if 14 < exotico < 21:
                ocupante = "15-20 Ffyrnig (aleatório)"
    ocupacaon = randint(1, 20)
    if ocupacaon < 19:
        ocupacao = "Ocupado"
    else:
        vaziomotiv = randint(1, 20)
        if 0 < vaziomotiv < 15:
            ocupacao = "Vazio\n" \
                       "Motivo:                 1-14 População Atacada (Rolar na tabela de encontro apropriada)"
        if 14 < vaziomotiv < 18:
            ocupacao = "Vazio\n" \
                       "Motivo:                 15-17 Abandono por escassez de recursos"
        if 17 < vaziomotiv < 21:
            ocupacao = "Vazio\n" \
                       "Motivo:                 18-20 Perigo Proximo (Rolar na tabela de monstruosidades apropriada)"
    espec1 = randint(1, 8)
    if tipoocupante < 11:
        if espec1 == 1:
            especi = "1 Coletores de especiarias raras"
        if espec1 == 2:
            especi = "2 Conhecidos por negociarem com forasteiros que parecem confiaveis"
        if espec1 == 3:
            especi = "3 Quase nenhum contato com o mundo externo"
        if espec1 == 4:
            especi = "4 Guerreiros implacaveis em busca de poder e territorio"
        if espec1 == 5:
            especi = "5 Estão ali há séculos"
        if espec1 == 6:
            especi = "6 Tem grande taxa de produção (+1 loja)"
        if espec1 == 7:
            especi = "7 Todos se conhecem, unidos como um clã"
        if espec1 == 8:
            especi = "8 Escravizados por alguma criatura"
    if 10 < tipoocupante < 14:
        if espec1 == 1:
            especi = "1 Quase nenhum contato com o mundo externo"
        if espec1 == 2:
            especi = "2 Grande maioria é composta por guerreiros tribais"
        if espec1 == 3:
            especi = "3 Lider xamã que prioriza a harmonia com a natureza"
        if espec1 == 4:
            especi = "4 Adoradores de algum deus ou criatura"
        if espec1 == 5:
            especi = "5 Estão na constante caça à elementais malignos"
        if espec1 == 6:
            especi = "6 Não tem apreço à matéria, valor, ou riqueza (sem comércio)"
        if espec1 == 7:
            especi = "7 Tem em seus objetivos encontrar relíquias de um artefato"
        if espec1 == 8:
            especi = "8 Escravizados por alguma criatura"
    if 13 < tipoocupante < 16:
        if espec1 == 1:
            especi = "1 Servem a uma criatura poderosa"
        if espec1 == 2:
            especi = "2 Grande maioria é composta por guerreiros tribais"
        if espec1 == 3:
            especi = "3 Veem forasteiros apenas como caça"
        if espec1 == 4:
            especi = "4 Saqueadores desordenados e comerciantes trapaceiros"
        if espec1 == 5:
            especi = "5 Espalhados em pequenos grupos por todo o territorio"
        if espec1 == 6:
            especi = "6 Guerreiros implacaveis em busca de poder e territorio"
        if espec1 == 7:
            especi = "7 Quase nenhum contato com o mundo externo"
        if espec1 == 8:
            especi = "8 Conhecidos por negociarem com forasteiros que parecem confiaveis"
    else:
        if espec1 == 1:
            especi = "1 Conhecidos por negociarem com forasteiros"
        if espec1 == 2:
            especi = "2 Quase nenhum contato com o mundo externo"
        if espec1 == 3:
            especi = "3 Grande maioria é composta por guerreiros tribais"
        if espec1 == 4:
            especi = "4 Lider xamã que prioriza a harmonia com a natureza"
        if espec1 == 5:
            especi = "5 Não tratam bem forasteiros"
        if espec1 == 6:
            especi = "6 Mantem uma relação amistosa, mas com segundas intenções"
        if espec1 == 7:
            especi = "7 Fiéis à crenças e costumes antigos"
        if espec1 == 8:
            especi = "8 Escravizados por alguma criatura"
    espec2 = randint(1, 8)
    if tipoocupante < 11:
        if espec2 == 1:
            especii = "1 Recebem aventureiros por conta de alguma construção"
        if espec2 == 2:
            especii = "2 Zigurate de um antigo deus da forja"
        if espec2 == 3:
            especii = "3 Caverna escavada por eles mesmos"
        if espec2 == 4:
            especii = "4 Fortificação com muitas armadilhas e salas trancadas	"
        if espec2 == 5:
            especii = "5 Local construido com proposito de guardar/proteger algo"
        if espec2 == 6:
            especii = "6 Mantém um comércio interno (+1 loja)"
        if espec2 == 7:
            especii = "7 Caverna labiríntica"
        if espec2 == 8:
            especii = "8 Casas e estruturas coladas à montanha (sem assentamento interno)"
    if 10 < tipoocupante < 14:
        if espec2 == 1:
            especii = "1 Não tem moradia fixa"
        if espec2 == 2:
            especii = "2 Ruína abandonada (Rolar na tabela de ruínas)"
        if espec2 == 3:
            especii = "3 Recebem aventureiros por conta de alguma construção"
        if espec2 == 4:
            especii = "4 Ruínas de outras civilizações parcialmente enterradas"
        if espec2 == 5:
            especii = "5 Não há construções, vivem ao ar livre"
        if espec2 == 6:
            especii = "6 Moradias rusticas feitas de couro e folhas"
        if espec2 == 7:
            especii = "7 Local construido com proposito de guardar/proteger algo"
        if espec2 == 8:
            especii = "8 Grandes e altas torres de observação"
    if 13 < tipoocupante < 16:
        if espec2 == 1:
            especii = "1 Vivem em tocas subterraneas"
        if espec2 == 2:
            especii = "2 Não tem moradia fixa"
        if espec2 == 3:
            especii = "3 Ruína abandonada (Rolar na tabela de ruínas)"
        if espec2 == 4:
            especii = "4 Posto avançado da legião"
        if espec2 == 5:
            especii = "5 Não há construções, vivem ao ar livre"
        if espec2 == 6:
            especii = "6 Cavernas subterraneas"
        if espec2 == 7:
            especii = "7 Fortificação com muitas armadilhas e salas trancadas"
        if espec2 == 8:
            especii = "8 Vila dominada de outros humanoides"
    else:
        if espec2 == 1:
            especii = "1 Vivem em tocas subterraneas"
        if espec2 == 2:
            especii = "2 Não tem moradia fixa"
        if espec2 == 3:
            especii = "3 Recebem aventureiros por conta de alguma construção"
        if espec2 == 4:
            especii = "4 Não há construções, vivem ao ar livre"
        if espec2 == 5:
            especii = "5 Ruína abandonada (Rolar na tabela de ruínas)"
        if espec2 == 6:
            especii = "6 Local construido com proposito de guardar/proteger algo"
        if espec2 == 7:
            especii = "7 Assentamento fortificado e isolado"
        if espec2 == 8:
            especii = "8 Abrigam diversos viajantes e mercadores"
    return assent, ocupante, ocupacao, especi, especii


def paisagemmundana():
    global paisagemV
    paisagem = randint(1, 100)
    if 0 < paisagem < 4:
        paisagemV = "1-3 Uma grande árvore é enfeitada com diversos ninhos de aves."
    if 3 < paisagem < 6:
        paisagemV = "4-5 Paredão de rochas que para parte da ventania"
    return paisagemV
# TERMINAR AS PAISAGENS
