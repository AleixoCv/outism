from db import createPlace, createUser
from constants import COMMON, COMPANY, ONG, TAB
from models import Address

def loadSignupView():
    while True:
        option = int(input("""
            O que você deseja cadastrar?\n
            1- Usuário comum
            2- Estabelecimento comercial
            3- ONG

            opção: """).strip())

        if option == 1:
            email = input(f"\n{TAB}# Digite seu email: ").strip()
            pwd = input(f"{TAB}# Digite sua senha: ").strip()

            createUser(email, pwd, COMMON)

            print(f"\n{TAB}# Usuário comum cadastrado com sucesso")

            break
        elif option == 2:
            cnpj = input(f"\n{TAB}# Digite o CNPJ do estabelecimento: ").strip()
            name = input(f"{TAB}# Digite o nome do estabelecimento: ").strip()
            description = input(f"{TAB}# Digite a descrição do estabelecimento: ").strip()
            category = input(f"{TAB}# Digite o tipo do estabelecimento: ").strip()
            neighborhood = input(f"{TAB}# Digite o bairro do estabelecimento: ").strip()
            lat, lng = input(f"{TAB}# Marque no mapa a coordenada do estabelecimento: ").strip().split(",")

            place = createPlace(cnpj, name, description, category, Address(neighborhood, lat, lng), COMPANY)

            while True:
                option = input(f"{TAB}# Deseja adicionar alguma vantagem do estabelecimento? (S/N): ").strip().lower()[0]
            
                if option == "s":
                    benefit = input(f"{TAB}# Digite a vantagem: ").strip()
                    place.addBenefit(benefit)
                else:
                    break

            option = input(f"{TAB}# Deseja adicionar um usuário para este estabelecimento? (S/N): ").strip().lower()[0]

            if option == "s":
                email = input(f"{TAB}# Digite o email do usuário: ").strip()
                pwd = input(f"{TAB}# Digite a senha do usuário: ").strip()

                createUser(email, pwd, COMPANY, cnpj)

            print(f"\n{TAB}# Estabelecimento comercial cadastrado com sucesso")
            break
        elif option == 3:
            cnpj = input(f"\n{TAB}# Digite o CNPJ da ONG: ").strip()
            name = input(f"{TAB}# Digite o nome da ONG: ").strip()
            description = input(f"{TAB}# Digite a descrição da ONG: ").strip()
            neighborhood = input(f"{TAB}# Digite o bairro da ONG: ").strip()
            lat, lng = input(f"{TAB}# Marque no mapa a coordenada da ONG: ").strip().split(",")

            place = createPlace(cnpj, name, description, None, Address(neighborhood, lat, lng), ONG)

            while True:
                option = input(f"{TAB}# Deseja adicionar algum projeto da ONG? (S/N): ").strip().lower()[0]
            
                if option == "s":
                    project = input(f"{TAB}# Digite o nome do projeto: ").strip()
                    place.addProjects(project)
                else:
                    break

            option = input(f"{TAB}# Deseja adicionar um usuário para esta ONG? (S/N): ").strip().lower()[0]

            if option == "s":
                email = input(f"{TAB}# Digite o email do usuário: ").strip()
                pwd = input(f"{TAB}# Digite a senha do usuário: ").strip()

                createUser(email, pwd, ONG, cnpj)

            print(f"\n{TAB}# Estabelecimento comercial cadastrado com sucesso")
            break
        else:
            print(f"\n{TAB}# Opção inválida")
            continue
    