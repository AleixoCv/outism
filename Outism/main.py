from constants import COMMON, COMPANY, ONG
from views.signinView import loadSigninView
from views.signupView import loadSignupView
from views.placesView import loadPlacesView
from views.ratingView import loadRatingView
from views.chatView import loadChatView


def main():
    user = None

    while True:
        if user == None:
            option = int(input("""
            O que você quer fazer?\n
            1- login
            2- cadastro

            opção: """).strip())

            if option == 1:
                user = loadSigninView()
            elif option == 2:
                loadSignupView()
            else:
                print("\nOpção inválida")
                continue

            if user == None:
                # caso o usuário não tenha sido autenticado ainda, volta para o menu inicial
                continue

        if user.profile == COMMON:
            option = int(input("""
            O que você quer fazer?\n
            1- Pesquisar locais
            2- Chat

            opção: """).strip())

            if option == 1:
                loadPlacesView(user)
                wanted = input("""Se você deseja procurar por um local específico \n
                Digite uma parte ou o nome do local que deseja buscar.""")

            elif option == 2:
                loadChatView(user.profile)
            else:
                print("\nOpção inválida")
                continue
        elif user.profile == COMPANY:
            option = int(input("""
            O que você quer fazer?\n
            1- Ver avaliações
            2- Chat

            opção: """).strip())

            if option == 1:
                loadRatingView()
            elif option == 2:
                loadChatView(user.profile)
            else:
                print("\nOpção inválida")
                continue
        elif user.profile == ONG:
            loadChatView(user.profile)


if __name__ == '__main__':
    main()
