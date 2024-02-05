import random  # Importe le module random pour générer des nombres aléatoires
import os  # Importe le module os pour interagir avec le système d'exploitation
from termcolor import colored  # Importe la fonction colored du module termcolor pour colorer le texte


def effacer_ecran():  # Définit une fonction pour effacer l'écran
    os.system(
        'cls' if os.name == 'nt' else 'clear')  # Utilise la commande système 'cls' pour Windows et 'clear' pour les autres systèmes


def afficher_tableau(code, suppositions, chances_restantes):  # Definition d'une fonction pour afficher le tableau dans le terminal
    effacer_ecran()  # Efface l'écran avant d'afficher le tableau

    # Définition d'une couleur en fonction du nombre de chances restantes
    if chances_restantes > 5:  # Si le nombre de chances restantes est supérieur à 5, la couleur est verte
        couleur_chances = 'green'
    elif 4 <= chances_restantes <= 5:  # Si le nombre de chances restantes est entre 4 et 5, la couleur est blanche
        couleur_chances = 'white'
    else:  # Sinon, la couleur est rouge
        couleur_chances = 'red'

    # Utiliser la fonction colored pour mettre en couleur le compteur de chances
    print("Bienvenue à Mastermind!")  # Affiche un message de bienvenue
    print("Vous devez trouver le code composé de 4 couleurs.")  # Explique les règles du jeu
    print(f"Les couleurs possibles sont Rouge, Vert, Bleu, Jaune, Blanc et Violet.")  # Liste les couleurs possibles
    print(colored(f"    | ? ? ? ? |     Chances restantes : {chances_restantes}",
                  couleur_chances))  # Affiche le nombre de chances restantes en couleur

    for supposition, feedback in suppositions:  # Pour chaque supposition et feedback dans la liste des suppositions
        feedback_couleurs = [
            colored(c, 'white', 'on_green') if c == 'G' else colored(c, 'white', 'on_yellow') if c == 'M' else colored(
                c, 'white') for c in
            feedback]  # Colorie le feedback en vert pour 'G', en jaune pour 'M' et en blanc pour '.'
        supposition_couleurs = [colored(c, couleur_lettre(c)) for c in
                                supposition]  # Colorie chaque lettre de la supposition selon sa couleur correspondante
        print(" ".join(feedback_couleurs[:2]) + " | " + " ".join(supposition_couleurs) + " | " + " ".join(
            feedback_couleurs[2:]))  # Affiche le feedback et la supposition colorés


def obtenir_supposition_utilisateur():  # Définit une fonction pour obtenir la supposition de l'utilisateur
    while True:  # Boucle infinie jusqu'à ce qu'une supposition valide soit entrée
        supposition = input(
            "Entrez votre code (R/G/B/Y/W/P): ").upper()  # Demande à l'utilisateur d'entrer sa supposition
        if all(couleur in 'RGBYWP' for couleur in supposition) and len(
                supposition) == 4:  # Si toutes les lettres de la supposition sont dans 'RGBYWP' et que la longueur de la supposition est 4
            return list(supposition)  # Retourne la supposition sous forme de liste
        else:  # Sinon
            print("Entrée invalide, essayez à nouveau.")  # Affiche un message d'erreur


def couleur_lettre(lettre):  # Définit une fonction pour obtenir la couleur correspondante à une lettre
    colors = {
        "R":"red",
        "G":"green",
        "B":"blue"
    }
    return colors[lettre]
    if lettre == 'R':  # Si la lettre est 'R', la couleur est rouge
        return 'red'
    elif lettre == 'G':  # Si la lettre est 'G', la couleur est verte
        return 'green'
    elif lettre == 'B':  # Si la lettre est 'B', la couleur est bleue
        return 'blue'
    elif lettre == 'Y':  # Si la lettre est 'Y', la couleur est jaune
        return 'yellow'
    elif lettre == 'W':  # Si la lettre est 'W', la couleur est blanche
        return 'white'
    elif lettre == 'P':  # Si la lettre est 'P', la couleur est magenta
        return 'magenta'
    else:  # Sinon, la couleur est blanche
        return 'white'


def generer_feedback(code, supposition):  # Définit une fonction pour générer le feedback
    feedback = []  # Crée une liste vide pour le feedback
    for i in range(4):  # Pour chaque indice de 0 à 3.
        if supposition[i] == code[
            i]:  # Si la lettre à l'indice i dans la supposition est égale à la lettre à l'indice i dans le code
            feedback.append('G')  # Ajoute 'G' au feedback
        elif supposition[i] in code:  # Sinon, si la lettre à l'indice i dans la supposition est dans le code
            feedback.append('M')  # Ajoute 'M' au feedback
        else:  # Sinon
            feedback.append('.')  # Ajoute '.' au feedback

    return feedback  # Retourne le feedback


def jouer_contre_ordi():  # Définit une fonction pour jouer contre l'ordinateur
    code = [random.choice('RGBYWP') for _ in range(4)]  # Génère un code aléatoire de 4 lettres parmi 'RVBJWP'
    suppositions = []  # Crée une liste vide pour les suppositions
    chances_restantes = 8  # Initialise le nombre de chances restantes à 8

    while chances_restantes > 0:  # Tant que le nombre de chances restantes est supérieur à 0
        afficher_tableau(code, suppositions, chances_restantes)  # Affiche le tableau de jeu
        supposition = obtenir_supposition_utilisateur()  # Obtient la supposition de l'utilisateur
        feedback = generer_feedback(code, supposition)  # Génère le feedback pour la supposition
        suppositions.append((supposition, feedback))  # Ajoute la supposition et le feedback à la liste des suppositions
        chances_restantes -= 1  # Décrémente le nombre de chances restantes de 1

        if feedback == ['G', 'G', 'G',
                        'G']:  # Si le feedback est ['G', 'G', 'G', 'G'], c'est-à-dire que l'utilisateur a trouvé le code
            afficher_tableau(code, suppositions, chances_restantes)  # Affiche le tableau de jeu
            print("Félicitations, vous avez trouvé le code!")  # Affiche un message de félicitations
            break  # Sort de la boucle
        elif chances_restantes == 0:  # Sinon, si le nombre de chances restantes est 0, c'est-à-dire que l'utilisateur a perdu
            afficher_tableau(code, suppositions, chances_restantes)  # Affiche le tableau de jeu
            print("Désolé, vous n'avez plus de chances. Le code était : {}".format(
                " ".join(code)))  # Affiche un message d'échec et le code
            break  # Sort de la boucle


def jouer_contre_humain():  # Définit une fonction pour jouer contre un autre humain
    code = obtenir_supposition_utilisateur()  # Obtient le code de l'utilisateur
    suppositions = []  # Crée une liste vide pour les suppositions
    chances_restantes = 8  # Initialise le nombre de chances restantes à 8

    while chances_restantes > 0:  # Tant que le nombre de chances restantes est supérieur à 0
        afficher_tableau(code, suppositions, chances_restantes)  # Affiche le tableau de jeu
        supposition = obtenir_supposition_utilisateur()  # Obtient la supposition de l'utilisateur
        feedback = generer_feedback(code, supposition)  # Génère le feedback pour la supposition
        suppositions.append((supposition, feedback))  # Ajoute la supposition et le feedback à la liste des suppositions
        chances_restantes -= 1  # Décrémente le nombre de chances restantes de 1

        if feedback == ['G', 'G', 'G','G']:
          # Si le feedback est ['G', 'G', 'G', 'G'], c'est-à-dire que l'utilisateur a trouvé le code
            afficher_tableau(code, suppositions, chances_restantes)  # Affiche le tableau de jeu
            print("Félicitations, vous avez trouvé le code!")  # Affiche un message de félicitations
            break  # Sort de la boucle
        elif chances_restantes == 0:  # Sinon, si le nombre de chances restantes est 0, c'est-à-dire que l'utilisateur a perdu
            afficher_tableau(code, suppositions, chances_restantes)  # Affiche le tableau de jeu
            print("Désolé, vous n'avez plus de chances. Le code était : {}".format(
                " ".join(code)))  # Affiche un message d'échec et le code
            break  # Sort de la boucle


if __name__ == "__main__":  # Si le script est exécuté directement
    choix = " "  # Initialise le choix à une chaîne vide
    while choix != 1 or choix != 2:  # Tant que le choix n'est ni 1 ni 2
        effacer_ecran()  # Efface l'écran
        print("Choisissez le mode de jeu :")  # Demande à l'utilisateur de choisir le mode de jeu
        print("1. Jouer contre l'ordinateur")  # Option 1 : jouer contre l'ordinateur
        print("2. Jouer contre un autre humain")  # Option 2 : jouer contre un autre humain
        choix = input("Entrez votre choix (1 ou 2) : ")  # Demande à l'utilisateur d'entrer son choix

        if choix == '1':  # Si le choix est 1
            jouer_contre_ordi()  # Joue contre l'ordinateur
        elif choix == '2':  # Si le choix est 2
            jouer_contre_humain()  # Joue contre un autre humain
        else:  # Sinon
            print("Choix invalide. Veuillez entrer 1 ou 2.")  # Affiche un message d'erreur
