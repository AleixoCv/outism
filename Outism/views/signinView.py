from data import users
from constants import TAB
from db import validateUser

def loadSigninView():
    while True:
        email = input(f"\n{TAB}# Digite seu email: ").strip()
        pwd = input(f"{TAB}# Digite sua senha: ").strip()

        user = validateUser(email, pwd)

        if user == None:
            print(f"\n{TAB}# Email ou senha inválidos")
            continue

        print(f"\n{TAB}# Acesso realizado com sucesso")
        return user