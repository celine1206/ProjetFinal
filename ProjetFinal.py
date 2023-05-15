import datetime

# cration de la classe Personne
class Personne(object):

    #le constructeur avec valeurs par defaut
    def __init__(self, nom : str = 'noname', prenom : str = 'noname'):
        self.set_nom(nom)
        self.set_prenom(prenom)

    #les methodes d'acces
    #pour nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, value):
        if len(value) <= 6 or len(value) >= 20:
            raise ValueError('La personne doit avoir un nom dune longueur de 6 a 20 caracteres.')
        if not value[0].isupper() or not all(c.isalpha() for c in value):
            raise ValueError('La personne doit avoir un nom qui commence par une lettre majuscule et qui contient que des lettres alphabetiques,')
        else:
            self.__nom = value

    #pour prenom
    def get_prenom(self):
        return  self.__prenom

    def set_prenom(self, value):
        if len(value) <= 6 or len(value) >= 20:
            raise ValueError('La personne doit avoir un prenom dune longueur de 6 a 20 caracteres.')
        if not value[0].isupper() or not all(c.isalpha() for c in value):
            raise ValueError('La personne doit avoir un prenom qui commence par une lettre majuscule et qui contient que des lettres alphabetiques,')
        else:
            self.__prenom = value

    #La méthode magique nommée "__str__".
    def __str__(self):
        return f'{self.set_nom}\n {self.set_prenom}'


#creation de la classe Employe
class Employe(Personne):

    #le constructeur
    def __int__(self, nom : str, prenom : str, code : int = 0, fonction : str = 'rien'):
        super().__init__(nom, prenom) #appel du constructeur du parent
        #appel des methodes set
        self.set_code(code)
        self.set_fonction(fonction)

    #les methodes d'acces
    #pour code
    def get_code(self):
        return self.__code

    def set_code(self, value):
        self.__code = value

    #pour fonction
    def get_fonction(self):
        return self.__fonction

    def set_fonction(self, value):
        self.__fonction = value


    #La méthode magique nommée "__str__".
    def __str__(self):
        return f'{super().__str__()}\n, {self.__code}\n, {self.__fonction}'


#creation de la classe Client
class Client(Personne):

    #le constructeur
    def __int__(self, nom : str, prenom : str, telephone : str, courriel : str):
        super().__init__(nom, prenom) #appel du constructeur du parent
        #appel des methodes set
        self.set_telephone(telephone)
        self.set_courriel(courriel)

    #les methodes d'acces
    #pour telephone
    def get_telephone(self):
        return self.__telephone

    def set_telephone(self, value):
        self.__telephone = value

    #pour courriel
    def get_courriel(self):
        return self.__courriel

    def set_courriel(self, value):
        self.__courriel = value


    #La méthode magique nommée "__str__".
    def __str__(self):
        return f'{super().__str__()}\n, {self.__telephone}\n, {self.__courriel}'


#creation de la classe reparation
class Reparation(object):

    #le constructeur
    def __init__(self, code : int = 0, description : str = 'rien', montant : float = 0, datereparation : datetime = '01/01/1111', codeemploye : int = 0):
        self.set_code(code)
        self.set_description(description)
        self.set_montant(montant)
        self.set_datereparation(datereparation)
        self.set_codeemploye(codeemploye)

    #les methodes d'acces
    #pour code
    def get_code(self):
        return self.__code

    def set_code(self, value):
        self.__code = value

    #pour description
    def get_description(self):
        return self.__description

    def set_description(self, value):
        self.__description = value

    #pour montant
    def get_montant(self):
        return self.__montant

    def set_montant(self, value):
        self.__montant = value

    #pour datereparation
    def get_datereparation(self):
        return self.__datereparation

    def set_datereparation(self, value):
        self.__datereparation = value

    #pour codeemploye
    def get_codeemploye(self):
        return self.__codeemploye

    def set_codeemploye(self, value):
        self.__codeemploye = value


