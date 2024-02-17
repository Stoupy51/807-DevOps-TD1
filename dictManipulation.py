class SuperDictionnaire(dict):
    
    def __init__(self, dico):
        assert type(dico) == dict, "Type invalide"
        assert len(dico) > 0, "Dictionnaire vide"
        self.dico = dico

    def uniques(self):
        valu = []
        for val in self.dico.values():
            if val not in valu:
                valu.append(val)
        return (valu)
    
    def supprimerDoublons(self):
        res = dict()
        for cle,val in self.dico.items():
            res.setdefault(val,cle)
        res = dict((k,v) for v,k in res.items())
        return res
    
#Tests unitaires

def test_init():
    try:
        assert SuperDictionnaire(3) == None, "Erreur de test init, l'argument n'est pas un dictionnaire mais a été accepté"
        assert SuperDictionnaire(dict())== None, "Erreur de test init, l'argument est un dictionnaire vide mais a été accepté"
    except:
        pass #on passe parce qu'on est supposé avoir une erreur
    assert SuperDictionnaire({1:2})!= None, "Erreur de test init, l'argument est un dictionnaire non vide mais a été refusé"
    
def test_uniques():
    assert SuperDictionnaire({1:2, 3:4, 5:6, 7:8}).uniques() == [2, 4, 6, 8], "Erreur de test uniques(), le résultat n'est pas correct"
    assert SuperDictionnaire({1:1, 2:1, 3:2, 4:2, 5:3}).uniques() == [1, 2, 3], "Erreur de test uniques(), le résultat n'est pas correct"

def test_supprimerDoublons():
    assert SuperDictionnaire({1:2, 3:4, 5:6, 7:8}).supprimerDoublons() == {1:2, 3:4, 5:6, 7:8}, "Erreur de test supprimerDoublons, le résultat n'est pas correct"
    assert SuperDictionnaire({1:1, 2:1, 3:2, 4:2, 5:3}).supprimerDoublons() == {1: 1, 3: 2, 5: 3}, "Erreur de test supprimerDoublons, le résultat n'est pas correct"
    assert SuperDictionnaire({1:'a', 2:'b',3:'b'}).supprimerDoublons() == {1:'a', 2: 'b'}, "Erreur de test supprimerDoublons, le résultat n'est pas correct"
    assert SuperDictionnaire({1:'a', 2:'b'}).supprimerDoublons() == {1:'a', 2: 'b'}, "Erreur de test supprimerDoublons, le résultat n'est pas correct"

if  __name__ == "__main__":
    test_init()
    test_uniques()
    test_supprimerDoublons()

