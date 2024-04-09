import winsound

while True:
    print("Bem vindo ao grande mundo de Whalbior!")
    print("Antes de iniciarmos sua aventura, me diga, qual dessas raças você deseja começar o jogo?\n"
          "Humano - Ponto forte dessa raça é a sua inteigencia (digite 'h')\n"
          "Homem-Macaco - Ponto forte dessa raça é a agilidade e habilidades dos macacos. (digite 'hm')\n" 
          "Homem-Peixe - Ponto forte é sua força e condições de peixe (digite 'hp')\n"
          "Doguinho Caramelo - Essa raça é apenas para quem deseja resenhar pelo mundo de Walbior (digite 'caramelo')")

    raça = input("Qual você escolhe? ")

    if raça.lower() == "h":
        sexoh = input("Você será Homem ou Mulher?")
        if(sexoh.lower() == "homem"):
            nick = input("Qual seu nome meu caro?")
            print("Ok {}, vamos começar a aventura!".format(nick))
            print("Você esta no centro da cidade e ja tem uma missão a sua espera")
            missao1 = input("Óla, me chamo Rub.\nPoderia me ajudar com uma missão?(sim/não)")
            if(missao1 == "sim"):
                print("Ótimo, vá ate a floresta densa e procure pela minha filha que sumiu a 2 dias. te garanto uma ótima recompensa!")
                meio = input("Você deseja ir de barco ou cavalo?")
                if(meio == "barco"):
                    print("Você escolheu ir de barco e chegou em 2 dias.")
                    print("Você se deparou com um pedaço de um vestido, deve ser da filha do homem.")
                    winsound.PlaySound("girl-scream.wav", winsound.SND_FILENAME)
                    print("Veja, ela esta sendo levada por um grupo de goblins")
                    while True:
                        ato = input("Você prefere lutar com eles ou segui-los desfarçadamente?(lutar/seguir)")
                        if(ato == "lutar"):
                            print("Você morreu por tentar lutar com todos, escolha certo agora")
                        else:
                            print("massa")
                            break


        else:
            nick = input("Qual seu nome minha cara?")
            print("Ok {}, vamos começar a aventura!".format(nick))
        break

    elif raça.lower() == "hm":
        sexo = input("Você será macho ou fêmea? ")
        if sexo.lower() == "macho":
            print("Você será um Homem-macaco!")
            break
        elif sexo.lower() == "fêmea":
            print("Você será uma Mulher-Macaca!")
            break

    elif raça.lower() == "hp":
        print("Ótimo, você será um Homem-Peixe!")
        break

    elif raça.lower() == "caramelo":
        print("Ótimo, você será o Doguinho Caramelo!\nVamos começar!")
        destino1 = input("Você chegou na praça e encantou a todos, um homem desconhecido aparece querendo te levar para a casa dele.\nVocê vai ou corre?(Vou/vou nada)")
        if(destino1.lower() == "vou"):
            print("Por ser um Doguinho Caramelo você foi de boinha com o homem.\nChegando lá você é muito bem recebido pela familia dele e já almoça junto") 

        else:
            print("Você se saiu e correu para a floresta")
            print("Chegando lá você se depara com um grupo de jovens degustando cogumelos\nEles começam a fazer carinho e você, como um cachorro faz, cheira e come um dos cogumelos.")
            print("Logo após isso todos ficam preocupados com você pois não sabem a reação que pode causar em um cachorro, mas, em questão de segundos começam a surgir alguns goblins violentos e todos começam a correr.")
            ato1 = input("Você começa a fugir também mas percebe que uma das jovens esta sendo raptada, você deixa pra lá ou vai salva-la?(salvar/fugir)")
            if(ato1.lower() == "salvar"):
                print("Você decidiu salvar a menina mas acaba cercado por dois goblins.\nMas assim que percebem que você é um doguinho caramelo eles te fazem muito carinho e vão embora") 
                print       
        break

    else:
        print("Essa raça não existe aqui, por gentileza, escolha uma das raças citadas ou escreva corretamente.\n")
