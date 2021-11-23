#simulando o arquivo do banco de dados SQlite

from models import Address, User, Place
from constants import COMMON, COMPANY, ONG

users = [
    User("user1@email.com", "abcdef", COMMON),
    User("user2@email.com", "123456", ONG),
    User("user3@email.com", "000000", COMPANY)
]

addresses = [
    Address("Boa Viagem", -8.119588295070074, -34.90509190912361),
    Address("Aflitos", -8.03696053618465, -34.9048777888169),
    Address("Espinheiro", -8.045582624505773, -34.89387325998182)
]

places = [
    Place(1, "Ri-Happy", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus lacus ipsum, sodales ultricies vestibulum id, rutrum nec elit.", "brinquedos", addresses[0], COMPANY, 4.5),
    Place(2, "Jaqueira", "Phasellus ullamcorper nisi sed arcu feugiat, id pharetra nulla faucibus. Nulla facilisi. Etiam sed nunc nec risus iaculis efficitur.", "parque", addresses[1], COMPANY, 4.9),
    Place(3, "Casa da Criança", "Maecenas justo dui, vehicula sed pellentesque vel, suscipit sit amet ligula. Sed eget diam aliquam erat maximus pretium vel et eros. Integer vel nunc purus.", "restaurante", addresses[2], ONG)
]

