from db import searchPlaces
from models import Place, User
from constants import ONG, TAB


def loadMap(places):  # chamar o GoogleMaps
    pins = []

    for place in places:  # p é a tupla q está na lista places, q vem do db
        pin = {"name": place.name, "lat": place.address.lat, "lng": place.address.lng}
        # varrer os p's de places e pegar nome do local, latitude e longitude e atulaizar o dicionário pin
        pins.append(pin)

    print(pins)  # na interface gráfica, o mapa seria impresso com os pins para ser visualizado


def loadPlacesView(user: User):
    while True:
        entrada = input(f"\n{TAB}Digite as info do lugar (nome, bairro ou categoria): ").strip()
        if entrada == 'voltar':  # simular o toque de volta para tela anterior
            break

        places = searchPlaces(entrada)
        placesName = []

        for i, place in enumerate(places):
            placesName.append(places[i].name)

        placePrint = findPlace(placesName, entrada)

        for i, place in enumerate(placePrint):
            print(f"{TAB}{i + 1}- ", end="")  # imprime a lista q aparece na tela como resultado da busca
            print(f"{placePrint[i]}", end="")  # imprime a lista q aparece na tela como resultado da busca
            print()

        while True:
            clique = int(input("""
                O que você quer fazer?\n
                1- favoritar
                2- avaliar
                3- ver mapa
                4- sair

                opção: """).strip())

            if clique == 1:
                index = int(input(
                    "Digite o número do local: ").strip())  # se tivesse tela, pra ser userfriendly, isso seria o toque no local e o user ñ precisa saber código
                # baseado no q ele digitou eu vou procurar na lista de places qual o ID do nome q ele digitou

                user.favouritePlace(places[index - 1])

                print(f"\n{TAB}# Local favoritado")
            elif clique == 2:
                index = int(input("Digite o número do local: ").strip())
                rating = int(input("Digite o nota: "))

                places[index - 1].rate(rating)

                print(f"\n{TAB}# Avaliação realizada")
            elif clique == 3:
                print(f"\n{TAB}# MAPA")
                loadMap(places)
            else:
                break


def findPlace(string_list, wanted):
    wanted_list = []
    for i in range(len(string_list)):
        stringCheck = string_list[i].lower()
        wanted = wanted.lower()
        if stringCheck.startswith(wanted):
            wanted_list.append(string_list[i])

    if wanted_list:
        return wanted_list
    else:
        return "Lugar não encontrado!"
