from Rounders import *
from Rotate_for_max import *

#Utilisations des test dexemple basique du site "codewars"

def test_rounders():
    print("Démarrage des tests pour Rounders")
    tests = [(15,20),(1234,1000),(1445,2000),(14,10),(99,100),(10,10)]
    for test in tests:
        result = tail_rounding(test[0])
        print(test[0],"=",test[1],":",result==test[1])
        if result!=test[1]:
            return False
    return True

def test_rotate_for_max():
    print("Démarrage des tests pour Rotate_for_max")
    tests = [(38458215,85821534),(195881031,988103115),(896219342,962193428),(69418307,94183076)]
    for test in tests:
        result = max_rot(test[0])
        print(test[0],"=",test[1],":",result==test[1])
        if result!=test[1]:
            return False
    return True

def main():
    test_rounders()
    test_rotate_for_max()

if __name__ == "__main__":
    main()