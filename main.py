#Fonction secondaire
"""Fonction qui détermine si un mot est un palindrome."""
def ispalindrome(p):
    """
    >>>ispalindrome("radar")
    True
    >>>ispalindrome("civique")
    False
    >>>ispalindrome("kayak")
    True
    """
    for i in range(0,(len(p)//2)):
        if p[i] != p[-(i+1)]:
            return False
    return True

#### Fonction principale


def main():
    """
    Fonction qui contient une liste de mots et verifie avec la fonction 
    ispalindrome si ce sont des palindromes.

    >>>main()
    radar True
    kayak True
    level True
    rotor True
    civique False
    deifie False
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
