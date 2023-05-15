import datetime
from pathlib import Path
import jsonpickle


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
    def __int__(self, nom : str, prenom : str, telephone : str = '000-000-0000', courriel : str = 'personne@cegep.com'):
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


#creation de la classe Voiture
class Voiture(object):

    #constructeur
    def __init__(self, numeroplaque : str = 'AAA-AAA', marque : str = 'rien', modele : str = 'rien', couleur : str = 'rien', annee : int = 1111, proprietaire : Client = ()):
        self.set_numeroplaque(numeroplaque)
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_couleur(couleur)
        self.set_annee(annee)
        self.set_proprietaire(proprietaire)
        self.__reparations : list[Reparation] = []

    #les methodes d'acces
    #pour numeroplaque
    def get_numeroplaque(self):
        return self.__numeroplaque

    def set_numeroplaque(self, value):
        self.__numeroplaque = value

    #pour marque
    def get_marque(self):
        return self.__marque

    def set_marque(self, value):
        self.__marque = value

    #pour modele
    def get_modele(self):
        return self.__modele

    def set_modele(self, value):
        self.__modele = value

    #pour couleur
    def get_couleur(self):
        return self.__couleur

    def set_couleur(self, value):
        self.__couleur = value

    #pour annee
    def get_annee(self):
        return self.__annee

    def set_annee(self, value):
        self.__annee = value

    #pour proprietaire
    def get_proprietaire(self):
        return self.__proprietaire

    def set_proprietaire(self, value: Client):
        self.__proprietaire = value

    #pour reparations
    def get_reparations(self):
        return self.__reparations

    def set_reparations(self, value: Reparation):
        self.__reparations = value


#cartion de la classe Garage
class Garage(object):

    #le constructeur
    def __int__(self, nom : str = 'rien', adresse : str = 'rien', telephone : str = 'rien'):
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.__employes : list [Employe] = []
        self.__voitures : list [Voiture] = []

    #methodes d'acces
    #pour nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, value):
        self.__nom = value

    #pour adresse
    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, value):
        self.__adresse = value

    #pour telephone
    def get_telephone(self):
        return self.__telephone

    def set_telephone(self, value):
        self.__telephone = value

    #pour employes
    def get_employes(self):
        return self.__employes

    def set_employes(self, value: Employe):
        self.__employes = value

    #pour voitures
    def get_voitures(self):
        return self.__voitures

    def set_voitures(self, value: Voiture):
        self.__voitures = value


    #les methodes utilitaires
    def ajoutervoiture(self, element : Voiture) -> None:
        self.__voitures.append(element)

    def getvoiture(self, numvoiture:str)->Voiture:
        if Voiture.get_numeroplaque() == numvoiture:
            return self.__voitures[numvoiture]

    def ajouterreparation(self, numvoiture:str, reparation:Reparation)->None:
        Voiture.get_reparations().append(numvoiture)

    def getreparation(self, numvoiture:str)-> Reparation:
        if Voiture.get_numeroplaque() == numvoiture:
            return Voiture.get_reparations[numvoiture]



class Fichier:
    #methodes de la classe
    #serialiser
    @classmethod
    def serialisergarage(cls, element: Garage, fichier: str)->None:
        #creer le stream
        path:Path = Path(fichier)
        stream = path.open('w') #en ecriture
        #serialiser l'enlement vers le fichier
        strjson : str = jsonpickle.encode(element, indent=4, separators=(',', ':'))
        stream.write(strjson)
        #fermer le stream
        stream.flush()
        stream.close()

    #deserialiser
    @classmethod
    def deserialisergarage(cls, fichier:str)->Garage:
        #creer le stream
        path:Path = Path(fichier)
        stream = path.open('r') #en lecture
        #deserialiser vers objet Garage
        strjson = stream.read()
        reponse : Garage = jsonpickle.decode(strjson)
        #fermer le stream
        stream.close()
        #retourner la valeur
        return reponse

