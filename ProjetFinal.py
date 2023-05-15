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

