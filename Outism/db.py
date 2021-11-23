from data import users, places
from models import User, Place, Address

def validateUser(email, pwd):
    #aqui faria uma chamada no banco de dados utilizando email e senha para recuperar o usuário
    #simulando uma consulta no banco de dados que verifica se existe usuário com o email e senha informado
    for user in users:
        if user.email == email and user.pwd == pwd:
            return user

    return None 

def createUser(email, pwd, profile, cnpj = None):
    # aqui faria uma chamada ao banco de dados para inserir o usuário
    # simulando a criação do usuário no banco de dados
    users.append(User(email, pwd, profile, cnpj))

def createPlace(cnpj, name, description, category, address:Address, type):
    # aqui faria uma chamada ao banco de dados para inserir o lugar
    # simulando a criação do lugar no banco de dados
    place = Place(cnpj, name, description, category, address, type)
    places.append(place)
    
    return place

def searchPlaces(key):
    # usar a key passada como parâmetro para filtrar os lugares do banco de dados
    return places # lista de lugares filtrados pela key
