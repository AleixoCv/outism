class Address:
    def __init__(self, neighborhood, lat, lng):
        self.neighborhood = neighborhood
        self.lat = lat
        self.lng = lng

class User:
    def __init__(self, email, pwd, profile, cnpj=None):
        self.email = email
        self.pwd = pwd
        self.profile = profile
        self.cnpj = cnpj

        self.favouritePlaces = []

    def favouritePlace(self, place):
        self.favouritePlaces.append(place)

class Place:
    def __init__(self, cnpj, name, description, category, address:Address, type, rating = 0):
        self.cnpj = cnpj
        self.name = name
        self.description = description
        self.category = category
        self.address = address
        self.type = type
        self.rating = rating

        self.numRatings = 0
        self.benefits = []
        self.projects = []

    def rate(self, rating):
        self.numRatings += 1

        totalRating = self.rating + rating

        self.rating = totalRating / self.numRatings

    def addBenefit(self, benefit):
        self.benefits.append(benefit)

    def addProjects(self, project):
        self.projects.append(project)
