def max_rot(n): #Pour un nombre donnée, effecture une rotation complete, puis en exclant le 1,2, 3éme entier... et retourne le plus grand de tous
    def rotate_left(n,i): #Effectue une rotation
        str_n = str(n)
        rotated = str_n[i:] + str_n[:i] #Pas bon
        return int(rotated)

    str_n = str(n)
    rotations = [n]
    for i in range(len(str_n) - 1): #Itération pour effectuer toutes les rotations
        n = rotate_left(n,i) 
        rotations.append(n)
    return max(rotations)    

def main():
    print(max_rot(62738245))

if __name__ == "__main__":
    main()