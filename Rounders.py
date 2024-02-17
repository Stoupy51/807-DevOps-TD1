def tail_rounding(number): #Fonction qui calcul pour un nombre donnée, un nombre ne comportant qu'un seul entier différent à 0 en utilisant un principe de tail_rounding
    number_str = str(number)
    for i in range(len(number_str) - 1, 0, -1): #Parcours itératif inverse de chaque nombre, sauf le premier
        digit = int(number_str[i]) 
        if digit >= 5: # ajout 1 a l'entier suivant et remplace celui ci par 0
            number_str = number_str[:i] + str(int(number_str[i-1]) + 1) + '0' * (len(number_str) - i - 1)
        else: #Remplace lentier par 0
            number_str = number_str[:i] + '0' * (len(number_str) - i)
    return int(number_str)

def main():
    print(tail_rounding(1351))

if __name__ == "__main__":
    main()