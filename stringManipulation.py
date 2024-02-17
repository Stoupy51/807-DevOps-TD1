lowerA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upperA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

class SuperChaine(str):

  def __init__(self, chaine):
    assert type(chaine) == str, "Type invalide" #renforcement
    assert len(chaine) > 0, "Chaine vide" #renforcement
    assert chaine.isalpha(), "Chaine non alphabétique" #renforcement
    self.chaine = chaine

  def majuscule(self):
    copie = ''
    for letter in self:
      if letter in lowerA:
        copie += upperA[lowerA.index(letter)]
      else:
        copie += letter
    return copie

  def miniscule(self):
    copie = ''
    for letter in self:
      if letter in upperA:
        copie += lowerA[upperA.index(letter)]
      else:
        copie += letter
    return copie

  def titre(self):
    copie = ''
    if self[0] in lowerA:
        copie += upperA[lowerA.index(self[0])]
    else:
      copie += self[0]
    for i in range(1,len(self)):
      if self[i] in upperA:
        copie += lowerA[upperA.index(self[i])]
      else:
        copie += self[i]
    return copie

#Implémentation des tests unitaires
def test_init():
  try:
    assert SuperChaine(3) == None, "Erreur de test init, l'argument n'est pas une chaîne de caractères mais a été accepté"
    assert SuperChaine('')== None, "Erreur de test init, l'argument est une chaîne de caractères vide mais a été accepté"
    assert SuperChaine('bonjour888')== None, "Erreur de test init, l'argument est une chaîne de caractères non alphabétique mais a été accepté"
  except:
        pass #on passe parce qu'on est supposé avoir une erreur
  assert SuperChaine('bonjour')!= None, "Erreur de test init, l'argument est une chaîne de caractères alphabétique mais a été refusé"

def test_majuscule():
  assert SuperChaine('bonjour').majuscule() ==  'BONJOUR', "Erreur de test majuscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('BONJOUR').majuscule() ==  'BONJOUR', "Erreur de test majuscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('Bonjour').majuscule() ==  'BONJOUR', "Erreur de test majuscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('bONJOUR').majuscule() ==  'BONJOUR', "Erreur de test majuscule, la chaîne n'est pas correctement transformée"

def test_miniscule():
  assert SuperChaine('bonjour').miniscule() ==  'bonjour', "Erreur de test miniscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('BONJOUR').miniscule() ==  'bonjour', "Erreur de test miniscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('Bonjour').miniscule() ==  'bonjour', "Erreur de test miniscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('bONJOUR').miniscule() ==  'bonjour', "Erreur de test miniscule, la chaîne n'est pas correctement transformée"
  assert SuperChaine('bONjOUR').miniscule() ==  'bonjour', "Erreur de test miniscule, la chaîne n'est pas correctement transformée"

def test_titre():
  assert SuperChaine('bonjour').titre() ==  'Bonjour', "Erreur de test titre, la chaîne n'est pas correctement transformée"
  assert SuperChaine('BONJOUR').titre() ==  'Bonjour', "Erreur de test titre, la chaîne n'est pas correctement transformée"
  assert SuperChaine('Bonjour').titre() ==  'Bonjour', "Erreur de test titre, la chaîne n'est pas correctement transformée"
  assert SuperChaine('bONJOUR').titre() ==  'Bonjour', "Erreur de test titre, la chaîne n'est pas correctement transformée"
  
if  __name__ == "__main__":
  test_init()
  test_majuscule()
  test_miniscule()
  test_titre()