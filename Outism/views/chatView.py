from constants import COMMON, COMPANY, ONG

def loadChatView(profile):
    inChat = True #Boolean pra saber se estou logado no chat
    checkErrors = True #Boolean pra evitar seleções indesejadas na escolha do login
    checkChatErrors = True #Boolean pra evitar seleções indesejadas na escolha do chat

    #select = input("Como você quer logar? 1- Usuário / 2- ONG / 3- Estabelecimento") #Necessário para definir com quem ele vai falar
    while checkErrors: #Check para evitar escolhas indesejadas
        if profile == COMMON:
            print("Você entrou na área de chats!")
            while inChat:
                chatSelect = input("Selecione com quem você quer conversar -\n"
                                "1- ONG\n"
                                "2- Estabelecimento")
                while checkChatErrors:
                    if chatSelect =='1':
                        msgUser = input("Digite sua mensagem: ")
                        print(msgUser)
                        print("ONG -\n"
                            "Obrigado por entrar em contato conosco, em alguns minutos "
                            "iremos lhe responder!")
                        msgUser = input("Se quiser sair do chat digite 0")
                        if msgUser == '0':
                            checkChatErrors = False

                    elif chatSelect == '2':
                        msgUser = input("Digite sua mensagem: ")
                        print(msgUser)
                        print("Estabelecimento -\n"
                            "Obrigado por entrar em contato conosco, em alguns minutos "
                            "iremos lhe responder!")
                        msgUser = input("Se quiser sair do chat digite 0")
                        if msgUser == '0':
                            checkChatErrors = False
                    else:
                        print("Por favor, selecione um chat válido")

                chatExit = input("Se quiser sair da zona de chat, digite 0!, se não digite 1")
                if chatExit == '0':
                    inChat = False
                    checkErrors = False

        elif profile == ONG:
            while inChat:
                chatSelect = input("Selecione com quem você quer conversar -\n"
                                "1- Usuário\n"
                                "2- Estabelecimento")
                while checkChatErrors:
                    if chatSelect == '1':
                        msgUser = input("Digite sua mensagem: ")
                        print(msgUser)
                        print("Usuário -\n"
                            "Obrigado por entrar em contato comigo, em alguns minutos "
                            "iremos lhe responder!")
                        msgUser = input("Se quiser sair do chat digite 0")
                        if msgUser == '0':
                            checkChatErrors = False

                    elif chatSelect == '2':
                        msgUser = input("Digite sua mensagem: ")
                        print(msgUser)
                        print("Estabelecimento -\n"
                            "Obrigado por entrar em contato conosco, em alguns minutos "
                            "iremos lhe responder!")
                        msgUser = input("Se quiser sair do chat digite 0")
                        if msgUser == '0':
                            checkChatErrors = False
                    else:
                        print("Por favor, selecione um chat válido")

                chatExit = input("Se quiser sair da zona de chat, digite 0!, se não digite 1")
                if chatExit == '0':
                    inChat = False
                    checkErrors = False

        elif profile == COMPANY:
            while inChat:
                chatSelect = input("Selecione com quem você quer conversar -\n"
                                "1- ONG\n"
                                "2- Estabelecimento")
                while checkChatErrors:
                    if chatSelect == '1':
                        msgUser = input("Digite sua mensagem: ")
                        print(msgUser)
                        print("ONG -\n"
                            "Obrigado por entrar em contato conosco, em alguns minutos "
                            "iremos lhe responder!")
                        msgUser = input("Se quiser sair do chat digite 0")
                        if msgUser == '0':
                            checkChatErrors = False

                    elif chatSelect == '2':
                        msgUser = input("Digite sua mensagem: ")
                        print(msgUser)
                        print("Usuário -\n"
                            "Obrigado por entrar em contato conosco, em alguns minutos "
                            "iremos lhe responder!")
                        msgUser = input("Se quiser sair do chat digite 0")
                        if msgUser == '0':
                            checkChatErrors = False
                    else:
                        print("Por favor, selecione um chat válido")

                chatExit = input("Se quiser sair da zona de chat, digite 0!, se não digite 1")
                if chatExit == '0':
                    inChat = False
                    checkErrors = False

        else:
            print("Selecione um login válido!")